from collections import Counter

text = "Not him old music think his found enjoy merry. Listening " \
       "acuteness dependent at or an. Apartments thoroughly unsatiable" \
       " terminated sex how themselves. She are ten hours wrong walls stand" \
       " early. Domestic perceive on an ladyship extended received do. Why " \
       "jennings our whatever his learning gay perceive. Is against no he without" \
       " subject. Bed connection unreserved preference partiality not unaffected." \
       " Years merit trees so think in hoped we as. Maids table how learn drift but " \
       "purse stand yet set. Music me house could among oh as their. Piqued our sister " \
       "shy nature almost his wicket. Hand dear so we hour to. He we be hastily offence " \
       "effects he service. Sympathize it projection ye insipidity celebrated my pianoforte" \
       " indulgence. Point his truth put style. Elegance exercise as laughing proposal " \
       "mistaken if. We up precaution an it solicitude acceptance invitation. Literature" \
       " admiration frequently indulgence announcing are who you her. Was least quick after" \
       " six. So it yourself repeated together cheerful. Neither it cordial so painful" \
       " picture studied if. Sex him position doubtful resolved boy expenses. Her" \
       " engrossed deficient northward and neglected favourite newspaper. But use" \
       " peculiar produced concerns ten. Ignorant saw her her drawings marriage " \
       "laughter. Case oh an that or away sigh do here upon. Acuteness you exquisite" \
       " ourselves now end forfeited. Enquire ye without it garrets up himself. " \
       "Interest our nor received followed was. Cultivated an up solicitude mr unpleasant. "

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

