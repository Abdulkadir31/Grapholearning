import random
def determine_baseline_angle(raw_baseline_angle):
    comment = ""

    # falling

    if (raw_baseline_angle >= 0.2):

        baseline_angle = 0

        comment = "DESCENDING"
        keywords = "Fatigue, depressions, disappointment, unhappiness, discouragement. obstinacy, determination"
        description = ["The baseline here is descending, which indicates the person suffers from fatigue, depressions, disappointment, unhappiness and discouragement. Furthermore, the person is determined and obstinate and has difficulty in giving up his/her concepts for others.","The descending baseline of the user here demonstrates the individual has the likelihood of having exhaustion, miseries, frustration, despondency and demoralization. Besides, the individual is resolved and headstrong and experiences issues in surrendering his/her ideas for other people.","As evident from the descending baseline, the handwriting suggests that the person has the possibility of suffering from torments, disappointment and discouragement. Also, the person can be stubborn and has a hard time in giving up his/her ideas for other people.","As evident from the descending baseline, the handwriting suggests that the person has the possibility of suffering from torments, disappointment and discouragement. Also, the person can be stubborn and has a hard time in giving up his/her ideas for other people."]
        d= random.randrange(0,4)
    # rising

    elif (raw_baseline_angle <= -0.3):

        baseline_angle = 1

        comment = "ASCENDING"
        keywords = "Buoyant spirit, ambition, optimism, restlessness"
        description = ["The baseline of the person is rising which suggests that he/she possesses buoyant spirit, is ambitious and often restless. He/She usually wants to escape the demands of routine. He/She is excitable and  quickly stirred to action. At times, he/she loses himself/herself to external influences.","The baseline of the individual is rising which recommends that he/she has light soul, is eager and frequently anxious. He/She for the most part needs to get away from the requests of schedule. He/She is sensitive and immediately stirred to activity. Now and again, he/she loses himself/herself to external influences.","The individual's baseline is rising that recommends him/her having a light soul and is often anxious. He/She needs to get away from the schedule requests for the most part. He/She is sensitive and stirred to activity immediately. Further, he/she loses himself/herself now and again to external influences.","The baseline of the person is rising that prescribes a light soul to him/her and is often on the edge. Usually he/she wants to escape routine demands. He/She is immediately touchy and mixed in action. Moreover, he/she sometimes loses himself/herself to external impacts."]
        d = random.randrange(0, 4)
    # straight

    else:

        baseline_angle = 2

        comment = "STRAIGHT"
        keywords = "Composure, orderliness, emotional stability, dependability, perseverance"
        description = ["The baseline of the person is straight, hence he/she has good composure and orderliness in his/her pursue. He/She also possesses emotional stability and can be a dependable individual. His/Her perseverance will be able to make him/her achieve his/her goals in spite of challenging obstacles.","The baseline of the individual is straight, henceforth he/she has great self-control and deliberateness in his/her pursue. He/She likewise has emotional steadiness and can be a trustworthy person. His/Her persistence will most likely influence him/her to accomplish his/her objectives disregarding difficult obstacles.","The baseline of the individual is straight, henceforth he/she has great self-control and deliberateness in his/her pursue. He/She likewise has emotional steadiness and can be a trustworthy person. His/Her persistence will most likely influence him/her to accomplish his/her objectives disregarding difficult obstacles.","The individual's baseline is straight, he/she has great self - control and deliberacy in his/her pursuit. He/She also has emotional steadfastness and can be a person of confidence. His/Her persistence is likely to influence him/her to achieve his/her goals regardless of difficult obstacles.","The person's baseline is straight, which indicates he/she has incredible self - control and deliberacy in his/her interests. He/She additionally has passionate immovability and can be an individual of certainty. His/Her steadiness is probably going to impact him/her to accomplish his/her objectives regardless of several obstructions."]
        d = random.randrange(0, 4)

    return baseline_angle, comment, description[d], keywords


def determine_top_margin(raw_top_margin):
    comment = ""

    # medium and bigger

    if (raw_top_margin >= 1.7):

        top_margin = 0

        comment = "MEDIUM OR BIGGER"
        keywords = "modest, formal, respects others, listener, communication skills, introvert, self control"
        description = ["The person's reaction is modest and formal suggested by the margin space. He/She respects others and knows how to listen and how to provide space for the others to communicate. In addition, he/she is an introvert and has self control.","The individual's response is modest and formal proposed by the edge space. He/She regards others and realizes how to tune in and how to give space to the others to communicate. Furthermore, he/she is a contemplative person and has self control.","The person's reaction is unassuming and formal proposed by the edge space. He/She respects others and acknowledges how to tune in and how to offer space to the others communicate well. Moreover, he/she is an insightful individual and has attentiveness.","The individual's response is unassuming and formal proposed by the edge space. He/She regards others and recognizes how to tune in and how to offer space to the others to pass on. Additionally, he/she is a savvy individual and has mindfulness."]
        d = random.randrange(0, 4)

    # narrow

    else:

        top_margin = 1

        comment = "NARROW"
        keywords = "needs attention, extrovert, trusts people, selfish, discourtesy, lack of culture"
        description = ["The person's inherent character here is flamboyant as indicated by the narrow upper margin in the handwriting. He/She is extrovert and has excessive trust in people. Often, he/she has a tendency to give into selfishness, discourtesy and lack of culture.","The individual's natural character here is flashy as demonstrated by the restricted upper edge in the penmanship. He/She is outgoing person and has excessive trust in individuals. Frequently, he/she tends to surrender to self-centeredness, impoliteness and absence of culture.","The person's regular character here is ostentatious as shown by the confined upper edge in the handwriting. He/She is friendly individual and has excessive trust in people. Every now and again, he/she will in general surrender to conceit, rudeness and lack of culture.","The individual's ordinary character here is showy as appeared by the limited upper edge in the handwriting. He/She is well disposed individual and has extravagant trust in individuals. Sometimes, he/she will as a rule surrender to pride, impoliteness and lack of culture."]

        d = random.randrange(0, 4)

    return top_margin, comment, description[d], keywords


def determine_letter_size(raw_letter_size):
    comment = ""

    # big

    if (raw_letter_size >= 18.0):

        letter_size = 0

        comment = "BIG"
        keywords = "extrovert, enjoys attention and admiration, don’t like to be alone, boldness, enthusiasm, optimism, boastfulness, restlessness, lack of concentration, lack of discipline, non compromising, non adjustable"
        description = ["The person’s big handwriting, suggests he/she is an extrovert. He/She  needs and enjoys attention and admiration; do not like to be alone. He/She can act with boldness, enthusiasm,and optimism, nonetheless is also capable of boastfulness, restlessness, and lack of concentration and discipline. Usually, he/she doesn’t like to compromise or adjust.","The individual's big sized penmanship, recommends he/she is an outgoing person. He/She needs and appreciates consideration and adoration; don't prefer to be distant from everyone else. He/She can act with strength, excitement, and positive thinking, but at the same time is fit for pretentiousness, anxiety, and absence of fixation and control. He/She doesn't prefer to bargain or change.","The person's big handwriting, suggests he/she is a friendly individual. He/She needs and acknowledges thought and reverence; don't want to be far off from every other person. He/She can act with quality, fervor, and positive reasoning, and yet is fit for self importance, nervousness, and lack of discipline and control. He/She doesn't want to deal or change.","The individual's size of handwriting, proposes he/she is a neighborly person. He/She needs and recognizes thought and adoration; would prefer not to be far away from each other individual. He/She can act with quality, intensity, and positive thinking, but then is fit for pomposity, anxiety, and lack of fixation and control. He/She wouldn't like to a or change."]
        d = random.randrange(0, 4)

    # small

    elif (raw_letter_size < 13.0):

        letter_size = 1

        comment = "SMALL"
        keywords = " introvert, introspective person, academic mentality, concentrate for long period, modest, organized, executive ability, Strong power drive, independent"
        description = ["The person’s small handwriting, advocate his/her introvert and introspective disposition. He/She has an academic mentality and can concentrate for long periods of time in their studies and projects.  Although he/she is modest, sometimes to the point of feelings of inferiority, his/her talent for detail and for organizing often gives him/her a good executive ability. Over and above that, he/she possess a strong power drive and is quite independent of what others think.","The individual's small penmanship, proposes he/she is a self observer just as a contemplative individual. He/She has a scholarly mindset and can think for extensive stretches of time in his/her investigations and projects. Despite the fact that he/she is modest, some of the time to the point of sentiments of mediocrity, his/her ability for detail and for sorting out regularly gives him/her a decent official capacity. Well beyond that, he/she have a solid power drive and is very free of what others think.","The person's little handwriting, proposes he/she is an astute individual similarly as an intelligent person. He/She has an insightful frame of mind and can center for broad stretches of time in his/her examinations and project. Regardless of the way that he/she is inconspicuous, every so often to the point of assumptions of average quality, his/her capacity for detail and for masterminding as often as possible gives him/her a nice authority limit. A long ways past that, he/she have a strong power drive and is free of what others think.","The individual's small penmanship, proposes he/she is a canny individual comparatively as a shrewd individual. He/She has a smart attitude and can concentrate for wide stretches of time in his/her examinations and undertakings. Despite how he/she is subtle, now and again to the point of suspicions of normal quality, his/her ability for detail and for planning as frequently as conceivable gives him/her a pleasant specialist limit. Far past that, he/she have a solid power drive and is free of what others think."]
        d = random.randrange(0, 4)

    # medium

    else:

        letter_size = 2

        comment = "MEDIUM"
        keywords = " balances all things, good adaptability ,balance of mind, practical, realistic"
        description = ["The person’s medium handwriting, implies he/she is a balancer of all things. He/She can fit into conventional or prevailing circumstances with adaptability and balance of mind. He/She is practical and realistic.","The individual's medium penmanship, proposes he/she is a balancer of all things. He/She can fit into regular or winning conditions with flexibility and parity of brain. He/She is useful and reasonable.","The person's medium handwriting, proposes he/she is a balancer of all things. He/She can fit into standard or winning conditions with adaptability and equality of brain. He/She is valuable and sensible.","The individual's medium penmanship, proposes he/she is a balancer of all things. He/She can fit into standard or prevailing conditions with flexibility and equity of brain. He/She is profitable and reasonable."]
        d = random.randrange(0, 4)

    return letter_size, comment, description[d], keywords


def determine_line_spacing(raw_line_spacing):
    comment = ""

    # big

    if (raw_line_spacing >= 3.5):

        line_spacing = 0

        comment = "BIG"
        keywords = "isolating nature, not social, fears contact and closeness, grandiose fantasies,untrusting, harbors suspicions, extravagance"
        description = ["The person often tends to isolating himself/herself from his/her environment, socially, psychologically, or both. He/She has grown to fear contact and closeness. However, he/she may have constructed grandiose fantasies for himself/herself that set him/her apart from others. In addition, his/her isolated behaviour, may harbor suspicions that keep him/her separate and untrusting. Distance between lines here, is also an indication of extravagance.","The individual frequently tends to secluding himself/herself from his/her condition, socially, mentally, or both. He/She has developed to fear contact and closeness. Notwithstanding, he/she may have built pretentious dreams for himself/herself that set him/her apart from others. What's more, his/her segregated conduct, may harbor doubts that keep him/her discrete and untrusting. Separation between lines here, is likewise a sign of indulgence.","The individual as often as possible tends to isolating himself/herself from his/her condition, socially, rationally, or both. He/She has created to fear contact and closeness. In any case, he/she may have constructed self-absorbed dreams for himself/herself that set him/her apart from others. Also, his/her isolated direct, may harbor questions that keep him/her discrete and untrusting. Division between lines here, is in like manner an indication of extravagance.","The person as regularly as possible tends to isolating himself/herself from his/her condition, socially, sanely, or both. He/She has made to fear contact and closeness. Regardless, he/she may have manufactured self-retained dreams for himself/herself that set him/her apart from others. Additionally, his/her detached direct, may harbor addresses that keep him/her discrete and untrusting. Division between lines here, is in like way a sign of extravagance."]
        d = random.randrange(0, 4)


    # small

    elif (raw_line_spacing < 2.0):

        line_spacing = 1

        comment = "SMALL"
        keywords = "confused thoughts and feelings, inner pressure of emotional reactions,constantly expressive through work, lively, forceful, creative, poor concentration"
        description = ["The person’s small line spacing indicates he/she is more confused about his/her thoughts and feelings. The inner pressure of many emotional reactions puts him/her in constant need of expressing himself/herself in words, actions, projects. He/She is lively, forceful, and often creative, but can suffer from a lack of clarity of purpose or from jumbled ideas and poor concentration.","The individual's little line spacing shows he/she is increasingly befuddled about his/her contemplations and sentiments. The inward weight of numerous emotional responses places him/her in steady need of conveying everything that needs to be conveyed in words, activities, ventures. He/She is enthusiastic, commanding, and regularly imaginative, however can experience the ill effects of an absence of lucidity of direction or from scattered thoughts and poor focus.","The person's little line spacing indicates he/she is progressively confused about his/her examinations and feelings. The internal load of various emotional reactions places him/her in relentless need of passing on everything that should be passed on in words, exercises, projects. He/She is eager, instructing, and normally innovative, anyway can encounter the evil impacts of a lack of clarity of heading or from dispersed contemplations and poor focus.","The individual's little line spacing shows he/she is continuously confused about his/her feelings and thoughts. The inner pressure of different anxious responses places him/her in steady need of passing on everything that ought to be passed on in words, actions, projects. He/She is excited, forceful, and typically creative, in any case can experience the insidious effects of a nonattendance of lucidity of heading or from scattered considerations and poor concentration."]
        d = random.randrange(0, 4)

    # medium

    else:

        line_spacing = 2

        comment = "MEDIUM"
        keywords = "dedicated to work, hardworking, attentive, careful, peaceful, adaptive,understanding nature, buid rapport quickly, planner, organized, clarity in work, mature,spontaneity"
        description = ["The person is dedicated to his/her work which is pointed out by the moderately narrow spacing he/she left between the lines. He/She is quite hardworking, attentive and careful. Mostly, he/she has his/her peace and is adaptive person. He/She is of understanding nature. He/She can build rapport very quickly. Planning and organization skills are excellent. He/She has clarity in whatever he/she is doing. It indicates a mature way of life. He/She has spontaneity.","The person’s small line spacing indicates he/she is more confused about his/her thoughts and feelings. The inner pressure of many emotional reactions puts him/her in constant need of expressing himself/herself in words, actions, projects. He/She is lively, forceful, and often creative, but can suffer from a lack of clarity of purpose or from jumbled ideas and poor concentration.","The person's little line spacing shows he/she is progressively dumbfounded about his/her thoughts and feelings. The inner load of various energetic reactions places him/her in reliable need of passing on everything that should be passed on in words, exercises, adventures. He/She is eager, ordering, and normally creative, but can encounter the evil impacts of a lack of clarity of purpose or from befuddled considerations and poor concentrations.","The individual's little line spacing here indicates he/she is continuously puzzled about his/her musings and emotions. The inward heap of different emotional responses places him/her in solid need of passing on everything that ought to be passed on in words or experiences. He/She is energetic, requesting, and typically imaginative, in any case can experience effects of a lack of clarity of purpose or from perplexed contemplations and poor center intrigue."]
        d = random.randrange(0, 4)


    return line_spacing, comment, description[d], keywords


def determine_word_spacing(raw_word_spacing):
    comment = ""

    # big

    if (raw_word_spacing > 2.0):

        word_spacing = 0

        comment = "BIG"
        keywords = "extravagant, has a need to be noticed"
        description = ["The person has wide word spacing which says he/she demands attention in an extravagant or exaggerated manner, stemming from a need to be noticed, to be important.","The person has wide word spacing that says he/she requires attention to be important in an extravagant or exaggerated manner, stemming from a need to be noticed.","The individual has wide word dividing that says he/she expects thoughtfulness regarding be imperative in an indulgent or overstated way, coming from a should be taken note."]
        d = random.randrange(0, 3)

    # small

    elif (raw_word_spacing < 1.2):

        word_spacing = 1

        comment = "SMALL"
        keywords = "selfish, craves constant attention"
        description = ["This person will crowd others for attention, craving constant contact and closeness which is indicated by his/her narrow space between words. Hence, he/she can be selfish in his/her demands and unwilling to give of his/her own time and energies to others.","This individual will swarm others for consideration, needing consistent contact and closeness which is shown by his/her narrow space between words. Consequently, he/she can be egotistical in his/her requests and reluctant to give of his/her own time and energies to other people.","This individual will swarm others for attention, requiring steady contact and closeness which is appeared by his/her thin space between words. Thus, he/she can be self important in his/her solicitations and hesitant to give of his/her own time and energies to other individuals."]
        d = random.randrange(0, 3)

    # medium

    else:

        word_spacing = 2

        comment = "MEDIUM"
        keywords = "mature, intelligent, organized"
        description = ["The well-balanced spacing here, gives evidence of the writer’s social maturity, intelligence, and inner organization. He/She will be able to deal flexibly and objectively with himself/herself and with other people.","Medium spacing here, gives proof of the writer’s social development, insight, and inward association. He/She will almost certainly bargain adaptably and unbiasedly with himself/herself and with other individuals.","Medium spacing here, gives evidence of the writer’s social improvement, understanding, and inner organization. He/She will be able to deal adaptably and impartially with himself/herself and with different people."]
        d = random.randrange(0, 3)

    return word_spacing, comment, description[d], keywords


def determine_pen_pressure(raw_pen_pressure):
    comment = ""

    # heavy

    if (raw_pen_pressure > 180.0):

        pen_pressure = 0

        comment = "HEAVY"
        keywords = "full energy, aggressive, high energy, aggressive, high ego, determined, dominating, expressive."
        description = ["The heavy pressure here indicates the person likes to make an impression. There is a great deal of energy available to him/her for his/her actions. He/She express in a heavy manner, and is strong willed, firm and easily excited to hot-blooded actions. He/She can inspire others. Negatively, he/she can be stern, stubborn and inclined to morose thoughts or depression. ","The heavy pressure here indicates the person likes to make an impression. There is a great deal of energy available to him/her for his/her actions. He/She express in a heavy manner, and is strong willed, firm and easily excited to hot-blooded actions. He/She can inspire others. Negatively, he/she can be stern, stubborn and inclined to morose thoughts or depression. ","The heavy pressure here demonstrates the individual likes to establish a connection. There is a lot of energy accessible to him/her for his/her activities. He/She express in an overwhelming way, and is solid willed, firm and effectively eager to hot-blooded activities. He/She can move others. Adversely, he/she can be stern and slanted to negative thoughts or wretchedness.","The heavy pressure here demonstrates the individual likes to set up an association. There is a ton of essentialness available to him/her for his/her actions. He/She express in a heavy manner, and is strong willed, firm and successfully anxious to hot-blooded actions. He/She can inspire others. Negatively, he/she can be stern, troublesome and inclined to dismal examinations or disheartening."]
        d = random.randrange(0, 4)

    # light

    elif (raw_pen_pressure < 151.0):

        pen_pressure = 1

        comment = "LIGHT"
        keywords = "low energy, non productive, prefers routine, complacent behaviour, non emotional, stressful upbringing"
        description = ["The light pressure here indicates his/her personality is sensitive and impressionable. There is often great creative ability, but the potential is seldom fulfilled as such writers seem unable to absorb their experiences. The willpower is not strong, so the light-pressure writer can easily succumb to the dominance of a heavier writer. He/She is generally tolerant and genial, and though he/she can lapse into superficiality, his/her lack of inhibition can be refreshing. He/She sometimes tends to refuse to be committed. Very light pressure frequently turns up in the writing of actors or actresses, who must be able to drop their own force of personality in order to play the role of another. ","The light pressure here indicates his/her personality is sensitive and impressionable. There is often great creative ability, but the potential is seldom fulfilled as such writers seem unable to absorb their experiences. The willpower is not strong, so he/she can easily succumb to the dominance of a heavier writer. He/She is generally tolerant and genial, and though he/she can lapse into superficiality, his/her lack of inhibition can be refreshing. He/She sometimes tends to refuse to be committed. Very light pressure frequently turns up in the writing of actors or actresses, who must be able to drop their own force of personality in order to play the role of another. ","The light pressure here shows his/her personality is delicate and susceptible. There is often  incredible imaginative capacity, however the potential is only occasionally satisfied in that capacity writers appear to be unfit to ingest their encounters. The self discipline isn't solid, so he/she can without much of a stretch capitulate to the predominance of a heavier writer. He/She is commonly tolerant and friendly, and however he/she can pass into superficiality, his/her absence of hindrance can be refreshing. He/She here and there will in general won't be submitted. Exceptionally light pressure much of the time turns up in the composition of performing artists or on-screen characters, who must most likely drop their very own power of identity so as to assume the job of another.","The light pressure here demonstrates his/her identity is fragile and powerless. There is regularly amazing creative limit, anyway the potential is just once in a while fulfilled in that limit creators give off an impression of being unfit to ingest their experiences. The self-restraint isn't strong, so he/she can without quite a bit of a stretch cede to the power of a heavier writer. He/She is generally tolerant and benevolent, and anyway he/she can go into detail, his/her lack of prevention can be animating. He/She all over will all in all won't be submitted. Especially light pressure a great part of the time turns up in the creation of performing craftsmen or on-screen characters, who should in all probability drop their own one of a kind intensity of personality to accept the activity of another."]
        d = random.randrange(0, 4)

    # medium

    else:

        pen_pressure = 2

        comment = "MEDIUM"
        keywords = "balancer, adaptable, great gelling capability, pacifier"
        description = ["The person writes with normal pressure and this norm between the extremes is an indication of healthy vitality and willpower. Holiday breaks are generally very important to him.","The individual writes with normal pressure and this standard between the limits means that solid energy and self control. Occasion breaks are commonly critical to him.","The individual writes with normal pressure and this standard between the points of confinement implies that strong energy and willpower. Event breaks are generally basic to him.","The individual writes with normal pressure  and this standard between the extremes  suggests that solid essentialness and watchfulness. Occasion breaks are commonly fundamental to him."]
        d = random.randrange(0, 4)

    return pen_pressure, comment, description[d], keywords


def determine_slant_angle(raw_slant_angle):
    comment = ""

    # extremely reclined

    if (raw_slant_angle == -45.0 or raw_slant_angle == -30.0):

        slant_angle = 0

        comment = "EXTREMELY RECLINED"
        keywords = "Very sensitive, excellent human beings,influence of mother, fear, defiance,   introversion lack of involvement, repression, self-absorption, cautious"
        description = ["The slant of the person is very rare. This person may have polished outer image, but is very sensitive in nature. Nevertheless, he/she is an excellent human being. Although, his/her behavior is very evasive and the emotional nature is withdrawn. He/She is out of touch with his/her environment and lives in the past. Mother identification is so strong that individual development is blocked. Emotionally, he/she is cold, yet may still seem sociable.","The inclination of the individual is very rare. This individual may have cleaned external picture, yet is touchy in nature. All things considered, he/she is an astounding person. Despite the fact that, his/her conduct is extremely sly and the enthusiastic nature is pulled back. He/She is distant from his/her condition and lives before. Mother recognizable proof is strong to the point that singular improvement is blocked. Inwardly, he/she is cold, yet may even now appear to be friendly.","The slant of the person is very rare. This person may have polished outer image, however is very touchy in nature. Nevertheless, he/she is an excellent human being. Although, his/her behavior is very evasive and the emotional nature is withdrawn. He/She is out of contact with his/her surroundings and lives in the past. Mother identification is so robust that individual development is blocked. Emotionally, he/she is cold, but may additionally still appear sociable."]
        d = random.randrange(0, 3)

    # a little reclined or moderately reclined

    elif (raw_slant_angle == -15.0 or raw_slant_angle == -5.0):

        slant_angle = 1

        comment = "A LITTLE OR MODERATELY RECLINED"
        keywords = "sedentary lifestyle, good in cooking, engineering skills, commitment phobic, introvert, very romantic"
        description = ["The little reclination in the slant indicates he/she somehow manage to be charming in social situations while remaining emotionally aloof and hence is also commitment phobic. Feelings are repressed and fears and anxieties are not acknowledged. He/She tends to be out of touch with himself/herself emotionally yet is self-absorbed at the same time. Most of the times, he/she feels an inward longing to be different and will give more to the development of inner abilities and resources than to emotional development. Often he/she has an immature attachment to the ideals and values of his/her mother figure, who has usually played the dominant role in shaping the social personality. Furthermore, he/she resists accepting progress or change.","The little reclination in the slant demonstrates he/she by one way or another figure out how to fascinate in social circumstances while remaining sincerely reserved and subsequently is additionally commitment phobic. Sentiments are repressed and fears and tensions are not recognized. He/She will in general be distant from himself/herself yet is self-consumed in the meantime. The majority of the occasions, he/she feels an internal yearning to appear as something else and will offer more to the advancement of inward capacities and assets than to emotional improvement. Regularly he/she has a immature connection to the goals and estimations of his/her mom figure, who has generally assumed the predominant job in forming the social identity. Moreover, he/she opposes accepting advancement or change.","The little reclination in the slant suggests he/she somehow manage to be charming in social conditions whilst remaining emotionally aloof and as a result is additionally commitment phobic. Feelings are repressed and fears and anxieties are not acknowledged. He/She tends to be out of contact with himself/herself emotionally yet is self-absorbed at the same time. Most of the times, he/she feels an inward longing to be different and will give more to the improvement of internal capabilities and assets than to emotional development. Often he/she has an immature attachment to the ideals and values of his/her mom figure, who has generally played the dominant function in shaping the social personality. Furthermore, he/she resists accepting development or change."]
        d = random.randrange(0, 3)

    # a little inclined

    elif (raw_slant_angle == 5.0 or raw_slant_angle == 15.0):

        slant_angle = 2

        comment = "A LITTLE INCLINED"
        keywords = "best, balances emotional as well as responsibility, excellent parenting, have great judging quality, impartial, great peacemakers"
        description = ["The person possesses normal slant which is an indication that he/she is normally sensitive and emotionally healthy, but modest with responses. Judgment and logic rule, yet more sympathy and compassion are expressed by him. The range of expression is seldom over demonstrative.","The individual’s slant is normal which means that he/she is ordinarily sensitive and candidly sound, however modest  with reactions. Judgment and rationale rule, yet more compassion and empathy are communicated by him. The scope of expression is only sometimes over demonstrative.","The person here has normal inclination which indicates that he/she is mainly delicate and candidly sound, however unobtrusive with reactions. Judgment and motive rule, yet greater compassion and empathy are communicated by using him. The scope of articulation is only on occasion over definite."]
        d = random.randrange(0, 3)

    # moderately inclined

    elif (raw_slant_angle == 30.0):

        slant_angle = 3

        comment = "MODERATELY INCLINED"
        keywords = "pampered, heart rules over head, very emotional, great friend circle"
        description = ["He/She is the type of person who can cry and laugh readily, give vent to his/her feelings, is future- and goal-oriented and have an ardent, affectionate, amiable and sensitive emotional nature as indicated by the moderately inclined slant. He/She will express his/her emotional self impulsively. Feelings will influence his/her decisions, and he/she is quick to react with elation or discouragement. Moreover, he/she has great social skills and tends to have prominent friend circle.","He/She is the type of person who is readily able to cry and laugh, give vent to his/her feelings, is forward-looking and goal-oriented and has an ardent, affectionate, friendly and sensitive emotional nature as indicated by the slant of moderation. He/She will be impulsively expressing his/her emotional self. Feelings will influence his/her decisions, and with elation or discouragement he/she is quick to react. Mo, he/she has great social skills and tends to have prominent friend circle.","He/She is the sort of individual who is promptly ready to cry and giggle, offer vent to his/her sentiments, is forward-looking and objective situated and has an affectionate, friendly, ardent and sentimental nature as shown by the inclination of balance. He/She will be hastily communicating his/her passionate self. Emotions will impact his/her choices, and with joy or debilitation he/she rushes to respond."]
        d = random.randrange(0, 3)

    # extremely inclined

    elif (raw_slant_angle == 45.0):

        slant_angle = 4

        comment = "EXTREMELY INCLINED"
        keywords = "pretentious, excellent emotional capability, people’s person, possesses good empathy, interfering"
        description = ["He/She has a volcano of emotional reactions: extremely ardent, passionate, jealous, easily offended, very demonstrative with affections, susceptible to hurt and can hate bitterly and with abandon. Furthermore, his/her ability to love is the same way- restless, unsettled, impulsive, capable of hysteria, wears himself/herself out, strongly influenced by likes and dislikes, can be stirred by as well as stirs other people's emotions, plunges into relationships or causes. He/She can be aptly described as ‘an emotional brushfire.","He/She has a volcano of emotional reactions: extremely ardent, passionate, jealous, easily offended, with affections very demonstrative, susceptible to hurt, bitterly hateful and abandoned. In addition, his/her ability to love is the same - restless, unsettled, impulsive, capable of hysteria, wearing out, strongly influenced by likes and dislikes, can be stirred by as well as stirred emotions of other people, plunged into relationships or causes.","He/She has a volcano of emotional reactions: extraordinarily ardent, passionate, jealous, effortlessly offended, very demonstrative with affections, inclined to hurt and can hate bitterly and with abandon. Furthermore, his/her potential to love is the same way- restless, unsettled, impulsive, prone to hysteria, wears himself/herself out, strongly influenced with the aid of likes and dislikes, can be stirred by means of as well as stirs different people's emotions, plunges into relationships or causes. He/She can be aptly described as ‘an emotional brushfire’."]
        d = random.randrange(0, 3)

    # straight

    elif (raw_slant_angle == 0.0):

        slant_angle = 5

        comment = "STRAIGHT"
        keywords = "business minded, head rules over heart, egoistic, logical, analytical, works best when alone."
        description = ["The person’s straight slant stipulates his/her head-over-heart emotional attitude. He/She is open to the experience of the moment, but his/her responses are cautious and considered. Here emotional expression is under control. The manner is undemonstrative, independent, detached and even indifferent. Once emotional control is lost it is quickly regained, hence he/she functions well in emergencies and makes a good leader or contented loner. In addition, he/she is self-interested and asks, “What can the situation do for me?”. In arguing a point, he/she will make an appeal to judgment rather than to emotion. Often he/she has a great deal of personal magnetism and a dry wit that is quite attractive.","The individual's straight inclination stipulates his/her head-over-heart passionate demeanor. He/She is available to the experience existing apart from everything else, except his/her reactions are careful and considered. Here passionate articulation is leveled out. The manner is undemonstrative, autonomous, segregated and even unconcerned. When enthusiastic control is lost it is immediately recaptured, consequently he/she works well in crises and makes a decent pioneer or satisfied introvert. What's more, he/she is self-interested and asks, 'What can the circumstance accomplish for me?'. In defending a point, he/she will give into judgment as opposed to feeling. Frequently he/she has a lot of individual attraction and a dry mind that is very alluring.","The person’s straight slant stipulates his/her head-over-heart emotional attitude. He/She is open to the journey of the moment, but his/her responses are cautious and considered. Here emotional expression is under control. The manner is undemonstrative, independent, detached and even indifferent. Once emotional manage is lost it is shortly regained, as a result he/she features well in emergencies and makes a good chief or contented loner. In addition, he/she is self-interested and asks, 'What can the state of affairs do for me?'. In arguing a point, he/she will make an appeal to judgment instead than to emotion. Often he/she has a extraordinary deal of private magnetism and a dry wit that is pretty attractive."]
        d = random.randrange(0, 3)

    # irregular

    # elif(raw_slant_angle == 180 ):

    else:

        slant_angle = 6

        comment = "IRREGULAR"
        keywords = "unsettled, inconsistent, erratic, fickle"
        description = ["The slant here is rather unstable which reveals he/she is unsettled and inconsistent. He/She is subject to the moods and thoughts of the moment. The emotional nature is erratic; you never know how he/she will react. He/She swings between repression and expression with a complete lack of prevailing attitude. His/Her nature is can be best described as nervous, undisciplined, capricious, excitable and lacking in good judgment or common sense. Inside, the person feels socially inferior and off-center.","The slant here is rather unstable which reveals he/she is unsettled and inconsistent. He/She is subject to the moods and thoughts of the moment. The emotional nature is erratic; you never know how he/she will react. He/She swings between repression and expression with a complete lack of prevailing attitude. His/Her nature is can be best described as nervous, undisciplined, capricious, excitable and lacking in good judgment or common sense. Inside, the person feels socially inferior and off-center.","The slant here is alternatively unstable which exhibits he/she is unsettled and inconsistent. He/She is challenge to the moods and ideas of the moment. The emotional nature is erratic; you never understand how he/she will react. He/She swings between repression and expression with a whole lack of prevailing attitude. His/Her nature is can be aptly described as nervous, undisciplined, capricious, excitable and lacking in precise judgment or frequent sense. Inside, the person feels socially inferior and off-center."]
        d = random.randrange(0, 3)

    return slant_angle, comment, description[d], keywords