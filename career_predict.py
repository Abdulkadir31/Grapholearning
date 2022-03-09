def career(traits):
    pressure = traits[3]
    LetterSize = traits[1]
    Margin = traits[0]
    LineSpacing = traits[2]
    Slant = traits[4]
    Characteristics = []

    ## Realistic
    if LetterSize == 2 or Slant == 1:
        Characteristics.append(" Food Preparation, Agriculture, Safety & Law Enforcement, Engineering, Hospitality, Tourism")

    ## Investigative
    if  Slant == 5 or Slant == 6 or LetterSize == 1:
        Characteristics.append(" Data Analysis, Social Science, Engineering, Administration, Accounting")

    ## Artistic
    if LetterSize == 0 or Slant == 0  or Slant == 4:
        Characteristics.append(" Drama, Dance, Music, Designing")

    ## Social
    if  Margin == 0 or Slant == 0 or Slant == 2 or Slant == 3:
        Characteristics.append(" Social Services, Nursing, Therapy, Education & Library Services, Sport")

    ## Enterprise
    if  LetterSize == 0 or Slant == 5:
        Characteristics.append(" Sales, Hospitality, Legal Practice, Administration, Finance, Designing, Tourism")

    ##Conventional
    if LetterSize == 1:
        Characteristics.append(" Finance, Administration, Computing, Accounting, Mining & Resources, Laboratory Technician")

    results = set(Characteristics)
    Characteristics = list(results)
    final_results = []
    print("Categories are :"+str(len(Characteristics)))
    for i in Characteristics:
        temp = i.split(',')
        final_results = final_results + temp;
    final_results = list(set(final_results))
    return final_results



# just for checking
# ans = career([1, 0, 1, 1, 5])
# for i in ans:
#     print(i)
