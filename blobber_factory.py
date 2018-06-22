from textblob import Blobber
from textblob.taggers import NLTKTagger

# used to combine commonly used taggers, chunkers, etc to keep code DRY
tb = Blobber(pos_tagger = NLTKTagger())

blob = tb("This is amazing!")
another_blob = tb("This sucks!")

blob.pos_tagger is another_blob.pos_tagger
