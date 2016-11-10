########################################################################
## File name: generate_readme.py                                      ##
## Author: Rick van Rheenen                                           ##
## Date created: 2016-04-14                                           ##
## Date last modified: 2016-04-16                                     ##
## Description: README.MD generator for OpenKattis github repository  ##
########################################################################
##
## Instructions: 
##      Execute from the root of the OpenKattis Folder containing 
##      the language folders which contain the problems. 
##      EG: python3 scripts/generate_readme.py > README.MD   
##
## Changelog:
##      2016-11-10:
##          Reformat and reorder texts, show points per language
##      
##      2016-19-10: 
##          Add possibility to get first n problems in a problemslist.
##          Highest rating problem changed to top3.
##      
## TODO: 
##      - catch failed cUrls
##      - document this script..
##      - seriously, document this script!

import os
import io
import random
import pycurl
from bs4 import BeautifulSoup
from operator import attrgetter

def make_readme(problems):
    '''print the readme'''
    print("# OpenKattis")
    print("\tMy solutions to the problems on https://open.kattis.com/.\n")
    print("\tPlease do not steal any of the solutions, for reference use only.\n")
    print("[&copy;](https://github.com/rvrheenen/OpenKattis/blob/master/license.txt) Rick van Rheenen")
    print("## Summary")

    solved_problems = problems.search("solved", True)
    solved_amount = solved_problems.count()

    print("#### Total solved: %s" % (str(solved_amount)))

    # Averages per language
    for lang in solved_problems.get_distinct_vars("language"):
        lang_problems = solved_problems.search("language", lang)
        print("###### Solved in %s: %d (%.2f%%) - [Total: %.2f, Average: %.2f]" % (\
            lang,\
            lang_problems.count(), \
            round((lang_problems.count() / solved_amount) * 100, 2), \
            lang_problems.get_total_score(), \
            lang_problems.get_total_score() / lang_problems.count()))
    
    print("#### Average score: %.2f" % (solved_problems.get_total_score()/solved_problems.count()) )
    print("#### Total score: %.2f" % (1 + solved_problems.get_total_score()) )
    
    # Top 3:
    print(make_table(["Problem", "Language", "Difficulty"], solved_problems.sort("difficulty", True).get(["link", "language", "difficulty"], 3), None, "Top 3 highest difficulty solved"))
    
    print("## Problems")
    # Solved problems list:
    print(make_table(["Problem", "Language", "Difficulty"], solved_problems.get(["link", "language", "difficulty"]), "lmm", "Solved Problems:"))
    # Unsolved problems list:
    print(make_table(["Problem", "Language", "Difficulty"], problems.search("solved", False).sort("difficulty").get(["link", "language", "difficulty"]), "lmm", "Unsolved Problems:"))

def main():
    make_readme(get_problems().sort())

def debug():
    problems = ProblemsList()
    problems.add(Problem("hello", "Python", True))
    problems.add(Problem("bst", "Java", True))
    make_readme(problems)

def make_table(head, rows, aligns=None, title=None):
    '''Generates a table with given input, returns String'''
    if len(rows.problems if isinstance(rows, ProblemsList) else rows) < 1:
        return ''
    table = "#### " + title + "\n" if title != None else ""
    table += make_table_row(head)
    align = parse_aligns(aligns if aligns != None else ("l" + "m"*(len(head)-1))) 
    table += make_table_row(align)
    if isinstance(rows, list):
        if not isinstance(rows[0], list):
            rows = [rows]
    for row in rows.get() if isinstance(rows, ProblemsList) else rows:
        table += make_table_row(row.get() if isinstance(row, Problem) else row)
    return table

def make_table_row(line):
    '''Generates a single table row from the input'''
    return "".join("| "+str(x)+ " " for x in line) + "|\n"

def parse_aligns(align):
    '''Converts a list or string of [l,r,m] into md syntax for table alignment, returns list'''
    ret = []
    markup = {'l':':---', 'm':':---:', 'r':'---:'}
    for k in align:
        ret.append(markup[k])
    return ret

def get_problems():
    '''finds all problems as Problems adds them to ProblemsList and returns ProblemsList'''
    known_languages = "C C# C++ Go Haskell Java Javascript Objective-C PHP Prolog Python Ruby".split()
    problems = ProblemsList()
    for lang in get_folders():
        if lang in known_languages:
            for problem_folder in get_folders(lang):
                listdir = os.listdir(get_path([lang,problem_folder]))
                if ".ignore" in listdir:
                    continue
                solved = False if ".unsolved" in listdir else True
                problems.add(Problem(problem_folder, lang, solved))
    return problems

def get_path(dir = None, path = None):
    '''Gets path from given dir and path. If none given returns root of file. Assumes root is parent directory.'''
    if path == None:
        path = os.path.abspath(".")
    if dir != None:
        if type(dir) == str:
            dir = [dir]
        for d in dir:
            path += os.sep + d
    return path

def get_folders(folder = None):
    '''Gets all folders in folder, returns as list'''
    dir = get_path(folder)
    return [d for d in os.listdir(dir) if d not in get_ignores() and os.path.isdir(get_path(d, dir)) and d[0] != "."]

def get_ignores():
    '''Gets all entries in the .gitignore, returns as list'''
    try:
        return [x.rstrip(os.sep) for x in open(get_path('.gitignore'),'r').read().splitlines()]
    except (OSError, IOError):
        return []


class Problem:
    '''An individual problem'''
    def __init__(self, id, language=None, solved=None):
        '''Creates a new Problem, with given parameters. id may also be a Problem, then its information will be copied. '''
        if isinstance(id, Problem):
            self.id = id.id
            self.language = id.language
            self.solved = id.solved
        else:
            self.id = id
            self.language = language
            self.solved = solved
        for x in self.scrape_kattis(self.id):
            setattr(self, x[0], x[1])
        setattr(self, "link", self.get_flink())

    def __repr__(self):
        return "[%s]" % "".join([x + ": " + str(getattr(self, x))+", " for x in vars(self)])[:-2]

    def get(self, atrrs = None):
        '''Get a problem, with all (default) or only a few of its attributes, returns list'''
        if atrrs == None:
            return [getattr(self, x) for x in self.get_var_names()]
        else:
            if type(atrrs) == str:
                atrrs = [atrrs] 
            return [getattr(self, x) for x in atrrs if x in self.get_var_names()]
    
    def get_var_names(self):
        '''Get the names of all this problems variables, returns list'''
        return [x for x in vars(self)]

    def scrape_kattis(self, pname=None):
        ''' Scrapes the OpenKattis site to get the needed data on this problem. 
            Returns list with lists: [atrrname, atrr]
            Current atrrnames: time, memory, difficulty, authors, source and name
        '''
        
        url = 'https://open.kattis.com/problems/' + (pname.lower() if pname != None else self.id)
        e = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEFUNCTION, e.write)
        c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)') #prevents browser banning
        c.perform()
        c.close()

        body = e.getvalue().decode('UTF-8')
        soup = BeautifulSoup(body, 'html.parser')

        kattis_attributes = []
        for s in soup.find_all("div", {"class": "sidebar-info"}):
            for p in s.find_all("p"):
                t = p.find_all(text=True)
                t = [x for x in t if x != "\n"]
                t[0] = "".join(x for x in t[0].strip().rstrip(':').lower().split(" ")[0] if x not in '(){}<>') #nasty
                if len(t) < 2 or t[0] in ['problem','license', 'download']:
                    continue
                if not t in kattis_attributes:
                    kattis_attributes.append(t)

        kattis_attributes.append(["url", url])
        kattis_attributes.append(["name", str(soup.title.string).replace("– Kattis, Kattis", "")])
        return kattis_attributes
    
    def get_flink(self):
        '''Get formatted link, returns string'''
        try:
            return "[%s] (%s)" % (self.name, self.url) 
        except AttributeError:
            return "[%s] (%s)" % (self.id, self.url) 


class ProblemsList:
    '''List of all problems'''

    def __init__(self, probs = None):
        '''Create new List of problems. If probs is given copy it.'''
        self.problems = [] if probs == None else probs.copy()

    def __repr__(self):
        return repr(self.problems)
        
    def add(self, problem):
        '''Add Problem to the list'''
        self.problems.append(problem)
    
    def get(self, atrrs = None, amount=0):
        '''Get all (default) or <amount> problems, with all (default) or only a few of its attributes, returns list of Problems.get()'''
        return [p.get(atrrs) for p in self.problems][:(amount if amount > 0 else self.count())]

    def sort(self, sortby="name", rv=False):
        '''Sorts the ProblemsList, returns self'''
        if self.count() == 0:
            return self
        if not hasattr(self.get_random(), sortby):
            sortby = "id"
        self.problems = sorted(self.problems, key=attrgetter(sortby), reverse=rv)
        return self

    def count(self, type = None, q = None):
        '''Count problems, count all if no type and q given, else count occurence of type=q, return int'''
        return len(self.problems) if type == None and q == None else self.search(type, q).count()

    def search(self, type, q):
        '''Find all occurence of type=q in problems, return ProblemsList'''
        return ProblemsList([x for x in self.problems if getattr(x, type) == q])

    def get_total_score(self, type=None, q=None):
        '''Count scores of problems, count all if no type and q given, else count score of type=q, return int'''
        count = 0
        for prob in (self.problems if type == None and q == None else self.search(type, q).problems):
            count += float(prob.get("difficulty")[0])
        return round(count,1)

    def get_distinct_vars(self, var):
        '''Returns all distinct occurrences of var in problems, returns list'''
        distinct = []
        for p in self.problems:
            a = getattr(p, var)
            if a not in distinct:
                distinct.append(a)
        return distinct

    def get_random(self):
        '''Returns random Problem'''
        if self.count() > 0:
            return self.problems[random.randrange(0, self.count())]
        return None

if __name__ == "__main__": main()