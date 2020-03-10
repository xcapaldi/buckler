import argparse
from sys import exit
import crossref_commons.retrieval

# parse the commandline input
parser = argparse.ArgumentParser()
parser.add_argument("source", type=str, help="search for the reference info of the DOI or website you input here")
#parser.add_argument("-l", "--biblatex", help="save reference info in biblatex format", action="store_true")
parser.add_argument("-p", "--path", type=str, help="write reference to the given file")
#parser.add_argument("-s", "--sort", help="sort the resulting bibtex file", action="store_true")
parser.add_argument("-c", "--confirm", help="do not ask for user confirmation to write to bib file", action="store_true")
args = parser.parse_args()

ref = args.source
path = args.path
no_confirm = args.confirm


#if args.biblatex:
#    print("biblatex format!")
#else:
#    print("bibtex format...")

#if args.path:
#    print(path)
#else:
#    print('no path')

#print(crossref_commons.retrieval.get_publication_as_refstring(ref, 'bibtex'))

# '10.5621/sciefictstud.40.2.0382'

# need to check inputs

def generate_key(raw_ref):
    """Generate a unique reference key using the last name of the first author, the year and the first non-trivial title word."""
    split_ref = raw_ref.split(', ')
    
    for field in split_ref:
        if field[:6] == "author":
            last_name = field[8:].lower()
        elif field[:4] == "year":
            year = field[6:-1]
        elif field[:5] == "title":
            title = field[7:-1]
        else:
            pass
    
    key = last_name + year + first_word(title)
    return key

def first_word(title):
    """Find the first word in a title that isn't an article or preposition."""
    split_title = title.split()
    articles = ['a', 'an', 'the', 'some']
    prepositions = ['aboard','about','above','across','after','against','along','amid','among','anti','around','as','at','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round','save','since','than','through','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without']

    for word in split_title:
        if word.lower() not in articles and word.lower() not in prepositions:
            return word.lower()

def format_reference(raw_ref, key):
    split_ref = raw_ref.split('}, ')
    # find the first bracket which should mark the beginning of the key
    first_bracket = split_ref[0].index('{')
    type = split_ref[0][1:first_bracket]
    # now save the first field
    first_field_start = first_bracket + split_ref[0][first_bracket:].index(' ') + 1
    first_field = split_ref[0][first_field_start:]
    # now reassemble the reference formatted nicely
    formatted_ref = ""
    # add the reference type
    formatted_ref += type
    # and the new key
    formatted_ref += key
    formatted_ref += ',\n '
    # and the first field
    formatted_ref += first_field
    formatted_ref += '},\n'

    # add remaining fields (except for the last one)
    for field in split_ref[1:-1]:
        formatted_ref += ' '
        formatted_ref += field
        formatted_ref += '},\n'

    # now add last field
    formatted_ref += ' '
    formatted_ref += split_ref[-1]
    formatted_ref += '\n'

    return formatted_ref

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
def add_reference(reference, path):
    # check if user does not want to confirm writing
    if not no_confirm:
        print(f"Do you want to add this reference to {path}?")
        save = input("> ")
    else:
        save = 'y'
    
    # open file in append mode
    if 'y' in save.lower():
        try:
            with open(path, 'a') as f:
                f.write(reference)
            print("Done!")
        except:
            print("This path is broken!")
            exit()
    else:
        exit()


# function to sort bibtex file

# get related?


# process lookup
raw = doi_lookup(ref)
key = generate_key(raw)
formatted_ref = format_reference(raw, key)
print(formatted_ref)

# check if user wants to write to file
if path:
    add_reference(formatted_ref, path)
