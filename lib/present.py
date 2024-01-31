class Present:
    def __init__(self):
        self.contents = None
    
    def wrap(self, contents):
        if self.contents is not None:
            raise AlreadyWrappedException("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise NoContentsWrappedException("No contents have been wrapped.")
        return self.contents
    

class AlreadyWrappedException(Exception):
    pass

class NoContentsWrappedException(Exception):
    pass