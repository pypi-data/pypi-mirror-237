import io
import os
from contextlib import contextmanager
from typing import (
    List,
    Iterable,
    Generator,
    Tuple,
    Callable,
    Optional,
    Sequence,
    IO,
    cast,
    Any,
    Sized,
    TypeVar,
)
from itertools import repeat
import abc


class ProgressInterface:
    """Interface for progress objects."""

    @abc.abstractmethod
    def update(self, completed_fraction: float) -> None:
        """Method to update the status of a progress object to a new
        fraction of completeness.
        :param float completed_fraction: fraction of completion value
            must be 0 <= completed_fraction <= 1.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_completed_fraction(self) -> float:
        """Property to get the current completed fraction of the progress
        interface, i.e. the current fraction of completion of the task.
        """
        raise NotImplementedError


T = TypeVar("T")


def progress_iter(
    iterable: Iterable[T],
    progress: Optional[ProgressInterface] = None,
    weights: Optional[Sequence[float]] = None,
    iterable_length: Optional[int] = None,
) -> Iterable[T]:
    """Add progress tracking through a ProgressInterface to an iterable object.
    :param iterable: iterable object to which progress tracking is added.
    :param progress: progress interface objects that will take care of
        progress tracking.
    :param weights: weights to be associated with each iteration of the input
        iterable object. If weights are not specified, all iterations are
        assumed to have equal weight.
    :param iterable_length: length of the iterable object. Only needed if the
        iterable does not have a __len__() method.
    :return: Yields from :iterable:
    """
    # Case 1: no progress interface was passed => no progress to track.
    if progress is None:
        yield from iterable

    # Case 2: Iterate over the input iterable wile updating the progress
    # interface. Essentially this loops (yield) through the iterable, and
    # at each iteration calls the update method on the ProgressInterface
    # object.
    # At the end, send signal that completion reached 100% to the progress
    # interface.
    else:
        yield from _progress_iter_common(
            _progress_wrapper, iterable, progress, weights, iterable_length
        )
        progress.update(1.0)


def progress_iter_with_sub_progress(
    iterable: Iterable[T],
    progress: Optional[ProgressInterface] = None,
    weights: Optional[Sequence[float]] = None,
    iterable_length: Optional[int] = None,
) -> Iterable[Tuple[T, Optional[ProgressInterface]]]:
    """Add progress tracking through a ProgressInterface to an iterable object.
    The difference with 'progress_iter' is that items of the returned iterable
    will now contain tuples consisting of the original item and a
    ProgressInterface object which tracks progress of the subtasks within the
    whole progress range.
    For input parameters, see 'progress_iter' function.
    """
    # If no progress interface was passed => no progress to track and the
    # function simply returns an iterable consisting of tuples of the input
    # iterable values and 'None'.
    if progress is None:
        return zip(iterable, repeat(None))

    # Return tuples of the original iterable values and an associated
    # ProgressInterface.
    return _progress_iter_common(
        _progress_wrapper_with_sub_progress,
        iterable,
        progress,
        weights,
        iterable_length,
    )


R = TypeVar("R")


def _progress_iter_common(
    wrapper: Callable[
        [ProgressInterface], Callable[[Tuple[T, Tuple[float, float]]], R]
    ],
    iterable: Iterable[T],
    progress: ProgressInterface,
    weights: Optional[Sequence[float]] = None,
    iterable_length: Optional[int] = None,
) -> Iterable[R]:
    """Iterate over all values in the input iterable and apply the specified
    wrapper function to them. The wrapper function must accept arguments that
    have the form (item, (start_position, stop)).
    """

    # If no weight were provided, assume equal weights for all iterations.
    if weights is None:
        if iterable_length is None:
            try:
                iterable_length = len(cast(Sized, iterable))
            except:
                raise ValueError(
                    "Iterable has no length attribute and no value was"
                    "passed for parameter [iterable_length] either."
                ) from None

        weights = (1,) * iterable_length

    # Create sub-ranges of the 0-1 range proportionally to the input weights.
    ranges = weights_to_ranges(weights)

    # Iterate over input iterator while each time calling the update method
    # of the associated progress interface. map applies the update_progress
    # function to all elements returned by zip.
    update_progress = wrapper(progress)
    return map(update_progress, zip(iterable, ranges))


def weights_to_ranges(
    weights: Sequence[float], start: float = 0.0
) -> Iterable[Tuple[float, float]]:
    """Splits the range (0.0, 1.0) into a number of sub-ranges equal to the
    number of weights, with the size of each sub-range proportional to the
    value of its weights.
    For instance, if weights = [2,1,1], the range 0-1 is split into 3 sub-
    ranges, where the first has twice the size of the second and third:
    (0.0, 0.5), (0.5, 0.75), (0.75, 1.0).
    """
    # Ensure that empty files are > 0 for progress computation
    safe_weights = [w or 1.0 for w in weights]
    sum_of_weights = sum(safe_weights)
    stop = safe_weights[0] / sum_of_weights
    yield (start, stop)
    for weight in safe_weights[1:]:
        start = stop
        stop += weight / sum_of_weights
        yield (start, stop)


def _progress_wrapper(
    progress: ProgressInterface,
) -> Callable[[Tuple[T, Tuple[float, float]]], T]:
    """Create a wrapper function that takes an 'item_with_range' input object
    and returns the bare input item (an iterable) and updates the progress
    interface with the 'start' position of the range associated to the item.
    An 'item_with_range' is a tuple that has the form (iterable, range), where
    iterable is the iterable for which we track progress and range is a tuple
    (start, stop) giving the range of completion fractions for the iterable.
    """

    def progress_wrapper(item_with_range: Tuple[T, Tuple[float, float]]) -> T:
        """item_with_range: iterable and its completion range
        :return: The bare item
        """
        item, (start, _stop) = item_with_range
        progress.update(start)
        return item

    return progress_wrapper


def _progress_wrapper_with_sub_progress(
    progress: ProgressInterface,
) -> Callable[[Tuple[T, Tuple[float, float]]], Tuple[T, Optional[ProgressInterface]],]:
    """Return a function that takes an 'item_with_range' and return the
    iterable item with an associated ProgressInterface that does automatic
    rescaling of its .update() method in the range of 'item_with_range'.
    """

    def progress_wrapper(
        item_with_range: Tuple[T, Tuple[float, float]]
    ) -> Tuple[T, Optional[ProgressInterface]]:
        """item_with_range: iterable and its completion range
        :return: A tuple consisting of the bare item and a ProgressInterface instance
        """
        iterable_item, (start, stop) = item_with_range
        sub_progress = scale_progress(progress, start, stop)
        return iterable_item, sub_progress

    return progress_wrapper


def scale_progress(
    progress: Optional[ProgressInterface], start: float, stop: float
) -> Optional[ProgressInterface]:
    """Create an instance of a ProgressInterface with a modified .update
    method that rescales the value of the 'completed_fraction' to be in the
    range (start, stop).
    Example: if we specify start=0.25, stop=0.5, the .update
    method of the new instance will rescale any 'completed_fraction' fraction
    value to the range 0.25 - 0.5. So calling .update(0.5) will in fact update
    the progress instance to 0.375 instead of 0.5, and update(1.0) will update
    the progress instance to 0.5 and not to 1.0.
    """
    if start > stop:
        raise ValueError("start > stop")
    if progress is None:
        return None

    # Narrow the type scope of the progress object for typing purposes.
    scaled_progress: ProgressInterface = progress

    # Define a new class that will be returned by the function. The .update
    # method is modified so it automatically rescales its inputs to the
    # desired range of values.
    class SubProgress(ProgressInterface):
        def update(self, completed_fraction: float) -> None:
            """Rescale the completed_fraction value so that its value is
            in the range [start-stop].
            """
            completed_fraction = min(completed_fraction, 1)
            scaled_progress.update(start + completed_fraction * (stop - start))

        def get_completed_fraction(self) -> float:
            """Rescale the completed fraction so that its value is in the
            range [start-stop].
            """
            completed_fraction = scaled_progress.get_completed_fraction()
            return (completed_fraction - start) / (stop - start)

    return SubProgress()


@contextmanager
def subprogress(
    progress: Optional[ProgressInterface], step_completion_increase: float
) -> Generator[Optional[ProgressInterface], None, None]:
    """Context manager for running a progress bar or a subset of a progress
    bar (i.e. a "scaled progress".
    Usage example:
    with subprogress(my_progress_bar, 0.3, 'step 2') as sub_progressbar:
        ...

    :param progress: progress interface for which to create a sub-progress.
    :param step_completion_increase: increase in completion associated to the
        current subprogress step of the progress interface. In example, if
        step_completion_increase = 0.3, then it means that the current
        subprogress step will contribute an increase of 0.3 to the completed
        fraction value of the progress interface. So if at the start of the
        subprogress step the completed fraction is 0.25, then at the end the
        value will be 0.55 (0.25 + 0.3).
    :return: A ProgressInterface instance covering the range starting at the
        current position of :progress: and advancing :step_completion_increase:
    :raises ValueError:
    """
    if progress is None:
        yield None
        return
    start = progress.get_completed_fraction()
    stop = start + step_completion_increase
    if stop > 1.0:
        raise ValueError(
            f"progress interface completion value cannot be > 1. "
            f"Value passed for 'completed_fraction_increase' "
            f"[{step_completion_increase}] is too large."
        )
    yield scale_progress(progress, start, stop)


class FileObjectProgress(IO[bytes]):
    """Wraps a file object

    All read operations will be tracked and passed to the ProgressInterface
    instance
    """

    def __init__(self, f_obj: IO[bytes], progress: ProgressInterface):
        self._f = f_obj
        original_pos = f_obj.tell()
        f_obj.seek(0, io.SEEK_END)
        total_size = f_obj.tell() - original_pos
        f_obj.seek(original_pos)
        self.progress = progress

        if total_size == 0:

            def update_pos() -> None:
                progress.update(1)

        else:

            def update_pos() -> None:
                progress.update((f_obj.tell() - original_pos) / total_size)

        @contextmanager
        def track_position() -> Generator[None, None, None]:
            yield None
            update_pos()

        self.track_position = track_position

        super().__init__()

    def __iter__(self) -> "FileObjectProgress":
        return self

    def __next__(self) -> bytes:
        with self.track_position():
            return self._f.__next__()

    def __enter__(self) -> "FileObjectProgress":
        self._f.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._f.__exit__(*args)

    def close(self) -> None:
        self._f.close()

    @property
    def mode(self) -> str:
        m: str = self._f.mode
        return m

    @property
    def name(self) -> str:
        return self._f.name

    @property
    def closed(self) -> bool:
        return self._f.closed

    def fileno(self) -> int:
        return self._f.fileno()

    def flush(self) -> None:
        self._f.flush()

    def isatty(self) -> bool:
        return self._f.isatty()

    def read(self, n: int = -1) -> bytes:
        with self.track_position():
            return self._f.read(n)

    def readable(self) -> bool:
        return self._f.readable()

    def readline(self, limit: int = -1) -> bytes:
        with self.track_position():
            return self._f.readline(limit)

    def readlines(self, hint: int = -1) -> List[bytes]:
        with self.track_position():
            return self._f.readlines(hint)

    def seek(self, offset: int, whence: int = 0) -> int:
        raise RuntimeError("Trying to seek in a FileObjectProgress")

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        return self._f.tell()

    def truncate(self, size: Optional[int] = None) -> int:
        return self._f.truncate(size)

    def writable(self) -> bool:
        return self._f.writable()

    def write(self, s: bytes) -> int:
        raise RuntimeError("Trying to write in a FileObjectProgress")

    def writelines(self, lines: Iterable[bytes]) -> None:
        raise RuntimeError("Trying to write in a FileObjectProgress")


def with_progress(f: IO[bytes], progress: Optional[ProgressInterface]) -> IO[bytes]:
    if progress is None:
        return f
    return FileObjectProgress(f, progress)


class Opener:
    """Wraps a file object

    Acts as a replacement for builtin `open` which only opens when
    `__enter__` is called on the object.
    This is needed when building a large list of file objects
    which in a first loop are only accessed for their file name
    and in a second loop are opened.
    Builtin `open` would already open the file on the open call,
    resulting in "OSError: [Errno 24] Too many open files" in
    the first loop
    """

    def __init__(
        self, f: str, mode: str, wrapper: Callable[[IO[bytes]], IO[bytes]] = lambda x: x
    ):
        self.name = f
        self.mode = mode
        self.encoding = None if "b" in self.mode else "utf-8"
        self._f: Optional[IO[bytes]] = None
        self.wrapper = wrapper

    def __enter__(self) -> IO[bytes]:
        self._f = open(self.name, self.mode, encoding=self.encoding)
        return self.wrapper(self._f.__enter__())

    def __exit__(self, *args: Any) -> None:
        if self._f is not None:
            self._f.__exit__(*args)


def progress_file_iter(
    files: List[str], mode: str, progress: Optional[ProgressInterface]
) -> Iterable[IO[bytes]]:
    """Associate, to each input file, a sub-progress object whose contribution
    to the increase in completion of the input progress object is proportional
    to the file's size. The output is an iterator of file objects with their
    associated sub-progress already backed-in.
    Example: this can be used to track progress when reading through a list
    of files. Each file that is read will then contribute to the increment in
    progress proportionally to its size.

    :param files: list of files to which progress should be associated.
    :param mode: file access mode, e.g. 'rb' or 'r'.
    :param progress: ProgressInterface to which the file objects are associated.
    :return: file objects with backed-in subprogress.
    """
    file_size = [float(os.path.getsize(f)) for f in files]
    files_with_progress = progress_iter_with_sub_progress(
        iterable=files, progress=progress, weights=file_size, iterable_length=len(files)
    )
    for file, sub_progress in files_with_progress:
        yield cast(
            IO[bytes],
            Opener(file, mode=mode, wrapper=with_progress_decorator(sub_progress)),
        )


def with_progress_decorator(
    progress: Optional[ProgressInterface],
) -> Callable[[IO[bytes]], IO[bytes]]:
    def _wrapper(f: IO[bytes]) -> IO[bytes]:
        return with_progress(f=f, progress=progress)

    return _wrapper
