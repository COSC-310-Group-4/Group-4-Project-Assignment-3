# This class takes your sentence and turns it into code for nerTrainer.py
# Please follow the 4 steps below to add your test case

# Step 1: Put your sentence here
sentence = "What is the bio of Michael Caine?"

# Step 2: put the EXACT spelling of the PERSON, MOVIE, ORGANIZATION from your sentence below
person = "Michael Caine" # Put the person name here
pLen = len(person)
pFirst = sentence.find(person)
pLast = pFirst + pLen

movie = "" # Put the movie name here
mLen = len(movie)
mFirst = sentence.find(movie)
mLast = mFirst + mLen

org = "" # Put the organization name here
oLen = len(org)
oFirst = sentence.find(org)
oLast = oFirst + oLen

# Step 3: Run the code
part1 = "(\"" + str(sentence) + "\""

part2 = ", {\"entities\": ["

lines = []
if person != "":
        pLine = "(" + str(pFirst) + ", " + str(pLast) + ", \"PERSON\")"
        lines.append(pLine)

if movie != "":
        mLine = "(" + str(mFirst) + ", " + str(mLast) + ", \"WORK_OF_ART\")"
        lines.append(mLine)
        
if org != "":
        oLine = "(" + str(oFirst) + ", " + str(oLast) + ", \"ORG\")"
        lines.append(oLine)

part3 = ", ".join(lines)
part4 = "]}),"     

print(str(part1) + str(part2) + str(part3) + str(part4))

# Step 4: Copy and paste the output into nerTrainer.py in TRAIN_DATA
