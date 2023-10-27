import abc
import numpy as np


class Embedding(abc.ABC):
    """
    Abstract class for all types of embeddings
    """

    def __init__(self, dim=32, zeros=False):
        self.embedding = None
        self.dim = dim
        self.shape = None
        self.zeros = zeros
        if self.zeros:
            self._init_with_zeros()

    @abc.abstractmethod
    def get_embedding(self, content):
        pass

    @abc.abstractmethod
    def get_shape(self):
        return self.shape

    def _init_with_zeros(self):
        self.embedding = np.zeros(self.dim)
        self.shape = self.embedding.shape

    def to_list(self):
        self.embedding = self.embedding.tolist()

    def __str__(self):
        return str(self.embedding)

    def __repr__(self):
        return f"Embedding base class with shape = {self.shape}"

    def __eq__(self, other):
        return isinstance(other, Embedding)


class OneDimEmbedding(Embedding):
    """
    Abstract class for One Dimensional embeddings
    """

    def __init__(self):
        super(OneDimEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, content):
        """
        Abstract method to get the embedding of an image
        Args:
        content: path to link to the content file
        Returns:
        numpy array representing the embedding of the image
        """
        pass

    @abc.abstractmethod
    def get_shape(self):
        """
        Abstract method to get the shape of the embedding
        Returns:
        tuple representing the shape of the embedding
        """
        pass


class TwoDimEmbedding(Embedding):
    """
    Abstract class for Two Dimensional embeddings
    """

    def __init__(self):
        super(TwoDimEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, content):
        """
        Abstract method to get the embedding of an image
        Args:
        content: path to link of the content
        Returns:
        numpy array of shape (embedding_size,)
        """
        pass

    @abc.abstractmethod
    def get_shape(self):
        """
        Abstract method to get the shape of the embedding
        Returns:
        tuple of integers representing the shape of the embedding
        """
        pass


class ImageEmbedding(OneDimEmbedding):
    """
    Abstract class for image embeddings
    """

    def __init__(self):
        super(ImageEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, image):
        pass

    @abc.abstractmethod
    def get_shape(self):
        pass


class VideoEmbedding(TwoDimEmbedding):
    """
    Abstract class for image embeddings
    """

    def __init__(self):
        super(TwoDimEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, video):
        pass

    @abc.abstractmethod
    def get_shape(self):
        pass


class AudioEmbedding(TwoDimEmbedding):
    """
    Abstract class for Audio Embeddings
    """

    def __init__(self):
        super(AudioEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, audio):
        pass

    @abc.abstractmethod
    def get_shape(self):
        pass


class TextEmbedding(TwoDimEmbedding):
    """
    Abstract class for Text Embeddings
    """

    def __init__(self):
        super(TextEmbedding, self).__init__()

    @abc.abstractmethod
    def get_embedding(self, text):
        pass

    @abc.abstractmethod
    def get_shape(self):
        pass
