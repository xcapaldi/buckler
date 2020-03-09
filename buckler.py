import argparse
from sys import exit
import crossref_commons.retrieval

# parse the commandline input
parser = argparse.ArgumentParser()
parser.add_argument("source", help="search for the reference info of the DOI or website you input here")
parser.add_argument("-l", "--biblatex", help="save reference info in biblatex format", action="store_true")
parser.add_argument("-p", "--path", type=str, help="write reference to the given file")
parser.add_argument("-s", "--sort", help="sort the resulting bibtex file", action="store_true")
args = parser.parse_args()

ref = args.source
path = args.path

if args.biblatex:
    print("biblatex format!")
else:
    print("bibtex format...")

if args.path:
    print(path)
else:
    print('no path')

print(crossref_commons.retrieval.get_publication_as_refstring(ref, 'bibtex'))

# '10.5621/sciefictstud.40.2.0382'

# need to check inputs

def generate_key(raw_ref):
    """Generate a unique reference key using the last name of the first author, the year and the first non-trivial title word."""
    split_ref = raw_ref.split(, )
    
    for field in split_ref:
        if field[:6] == "author":
            last_name = field[8:]
        elif field[:4] == "year":
            year = field[6:]
        elif field[:5] == "title":
            title = field[7:-1]
        else:
            pass
    
    title_word = first_word(title)
    key = last_name + year + title_word
    return key

def first_word(title)
    """Find the first word in a title that isn't an article or preposition."""
    split_title = title.split()
    articles = ['a', 'an', 'the', 'some']
    prepositions = ['aboard','about','above','across','after','against','along','amid','among','anti','around','as','at','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round','save','since','than','through','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without']
   
   for word in title:
        if word.lower() not in articles and not in prepositions:
            return word.lower()

# function to look up reference
def doi_lookup(doi):
    """Use crossref to retrieve natbib reference information."""
    try:
        raw_ref = crossref_commons.retrieval.get_publication_as_refstring(doi, 'bibtex')
    except:
        print("Your DOI key didn't return any result or was not formatted properly!")
        exit()
    return raw_ref

# function to write reference to bibtex file

# function to sort bibtex file



