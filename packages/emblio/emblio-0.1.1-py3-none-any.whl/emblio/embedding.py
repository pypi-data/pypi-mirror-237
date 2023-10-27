import abc

class Embedding(abc.ABC):
    """
    Abstract class for all types of embeddings
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_embedding(self, content):
        pass

    @abc.abstractmethod
    def shape(self):
        pass

    def __str__(self):
        return "Embedding base class"
    
    def __repr__(self):
        return "Embedding base class"
    
    def __eq__(self, other):
        return isinstance(other, Embedding)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __copy__(self):
        return self.__class__()
    
    def __deepcopy__(self, memo):
        return self.__class__()
    
    def __getstate__(self):
        return {}
    
    def __setstate__(self, state):
        return self.__class__()
    
    def __reduce__(self):
        return self.__class__(), tuple()
    
class ImageEmbedding(Embedding):
    """
    Abstract class for image embeddings
    """
    def __init__(self):
        super(ImageEmbedding, self).__init__()
    
    @abc.abstractmethod
    def get_embedding(self, image):
        pass
    
    @abc.abstractmethod
    def shape(self):
        pass
    
    def __str__(self):
        return "ImageEmbedding base class"
    
    def __repr__(self):
        return "ImageEmbedding base class"
    
    def __eq__(self, other):
        return isinstance(other, ImageEmbedding)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __copy__(self):
        return self.__class__()
    
    def __deepcopy__(self, memo):
        return self.__class__()
    
    def __getstate__(self):
        return {}
    
    def __setstate__(self, state):
        return self.__class__()
    
    def __reduce__(self):
        return self.__class__(), tuple()

class VideoEmbedding(Embedding):
    """
    Abstract class for video embeddings
    """
    def __init__(self):
        super(VideoEmbedding, self).__init__()
    
    @abc.abstractmethod
    def get_embedding(self, video):
        pass
    
    @abc.abstractmethod
    def shape(self):
        pass
    
    def __str__(self):
        return "VideoEmbedding base class"
    
    def __repr__(self):
        return "VideoEmbedding base class"
    
    def __eq__(self, other):
        return isinstance(other, VideoEmbedding)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __copy__(self):
        return self.__class__()
    
    def __deepcopy__(self, memo):
        return self.__class__()
    
    def __getstate__(self):
        return {}
    
    def __setstate__(self, state):
        return self.__class__()
    
    def __reduce__(self):
        return self.__class__(), tuple()
    
class AudioEmbedding(Embedding):
    """
    Abstract class for audio embeddings
    """
    def __init__(self):
        super(AudioEmbedding, self).__init__()
    
    @abc.abstractmethod
    def get_embedding(self, audio):
        pass
    
    @abc.abstractmethod
    def shape(self):
        pass
    
    def __str__(self):
        return "AudioEmbedding base class"
    
    def __repr__(self):
        return "AudioEmbedding base class"
    
    def __eq__(self, other):
        return isinstance(other, AudioEmbedding)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __copy__(self):
        return self.__class__()
    
    def __deepcopy__(self, memo):
        return self.__class__()
    
    def __getstate__(self):
        return {}
    
    def __setstate__(self, state):
        return self.__class__()
    
    def __reduce__(self):
        return self.__class__(), tuple()

class TextEmbedding(Embedding):
    """
    Abstract class for text embeddings
    """
    def __init__(self):
        super(TextEmbedding, self).__init__()
    
    @abc.abstractmethod
    def get_embedding(self, text):
        pass
    
    @abc.abstractmethod
    def shape(self):
        pass
    
    def __str__(self):
        return "TextEmbedding base class"
    
    def __repr__(self):
        return "TextEmbedding base class"
    
    def __eq__(self, other):
        return isinstance(other, TextEmbedding)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())
    
    def __copy__(self):
        return self.__class__()
    
    def __deepcopy__(self, memo):
        return self.__class__()
    
    def __getstate__(self):
        return {}
    
    def __setstate__(self, state):
        return self.__class__()
    
    def __reduce__(self):
        return self.__class__(), tuple()