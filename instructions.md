Does the learner answer provide the same information as the correct answer? Be sure the learner answer provides enough detail to fully answer the question. See below for examples.

| Context   	|	 In 1940, Seabrook Island, South Carolina, Noah Calhoun is smitten with 17 year old heiress Allison "Allie " Hamilton after seeing her at a carnival, and they have a summer love affair. Noah takes Allie to an abandoned house that he intends to buy for them. They try to make love, but are interrupted by Noah's friend Fin with the news that Allie's parents have the police looking for her. |
| Question  	|	where is the notebook supposed to take place |
| Learner Answer	|	abandoned house |
| Correct Answer   	|	['seabrook island south carolina'] |
| Correctness	|	Incorrect |
| Reason    	|	The model output is completely unrelated to the correct answer. |

| Context   	|	 Borg won his fifth consecutive Wimbledon singles title, the 1980 Wimbledon Men's Singles final, by defeating McEnroe in a five - set match, often cited as the best Wimbledon final ever played -- the only comparable match being the 2008 Federer -- Nadal final. Having lost the opening set to an all - out McEnroe assault, Borg took the next two and had two championship points at 5 -- 4 in the fourth. However, McEnroe averted disaster and went on to level the match in Wimbledon's most memorable 34 - point tiebreaker, which he won 18 -- 16. In the fourth - set tiebreak, McEnroe saved five match points, and Borg six set points, before McEnroe won the set. Björn served first to begin the 5th set and fell behind 15 -- 40. Borg then won 19 straight points on serve in the deciding set and prevailed after 3 hours, 53 minutes. Borg himself commented years later that this was the first time that he was afraid that he would lose, as well as feeling that it was the beginning of the end of his dominance. |
| Question  	|	 how many wimbledons did borg win in a row |
| Learner Answer	|	 fifth |
| Correct Answer   	|	 ['five'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output is a gramatically invalid answer to the question. |

| Context   	|	 In biochemistry and metabolism, beta - oxidation is the catabolic process by which fatty acid molecules are broken down in the cytosol in prokaryotes and in the mitochondria in eukaryotes to generate acetyl - CoA, which enters the citric acid cycle, and NADH and FADH, which are co-enzymes used in the electron transport chain. It is named as such because the beta carbon of the fatty acid undergoes oxidation to a carbonyl group. Beta - oxidation is primarily facilitated by the mitochondrial trifunctional protein, an enzyme complex associated with the inner mitochondrial membrane, although some fatty acids are oxidized in peroxisomes.  |
| Question  	|	 where does b oxidation of fatty acids occur |
| Learner Answer	|	 in the cytosol |
| Correct Answer   	|	 ['in the cytosol in prokaryotes and in the mitochondria in eukaryotes'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output does not provide enough information and incorrect for eukaryotes |
 
| Context   	|	 The Citizenship Clause overruled the Supreme Court's Dred Scott decision that black people were not citizens and could not become citizens, nor enjoy the benefits of citizenship. Some members of Congress voted for the Fourteenth Amendment in order to eliminate doubts about the constitutionality of the Civil Rights Act of 1866, or to ensure that no subsequent Congress could later repeal or alter the main provisions of that Act. The Civil Rights Act of 1866 had granted citizenship to all persons born in the United States if they were not subject to a foreign power, and this clause of the Fourteenth Amendment constitutionalized this rule.  |
| Question  	|	 ratified by the states in 1868 the fourteenth amendment granted full citizenship rights to |
| Learner Answer	|	 all persons born in the united states |
| Correct Answer   	|	 ['all persons born in the united states if they were not subject to a foreign power'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output does not provide enough nuance |
 
| Context   	|	 The Oregon Medical Insurance Pool  (OMIP), instituted in 1987, is designed to provide medical insurance coverage for residents of the state of Oregon with pre-existing conditions  (i.e. HIV / AIDS, diabetes, etc.) who do not already have private insurance. OMIP is administered by Oregon's Office of Private Health Partnerships through Blue Cross / Blue Shield. It functions similarly to other private insurance.  |
| Question  	|	 who does the oregon medical insurance pool protect |
| Learner Answer	|	 residents of the state of oregon with preexisting conditions |
| Correct Answer   	|	 ['residents of the state of oregon with preexisting conditions ie hiv aids diabetes etc who do not already have private insurance'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output does not provide enough nuance |
 
| Context   	|	 Much of the city's tax base dissipated, leading to problems with funding education, sanitation, and traffic control within the city limits. In addition, residents in unincorporated suburbs had difficulty obtaining municipal services, such as sewage and building code enforcement. In 1958, a study recommended that the city of Jacksonville begin annexing outlying communities in order to create the needed tax base to improve services throughout the county. Voters outside the city limits rejected annexation plans in six referendums between 1960 and 1965. |
| Question  	|	 What was the cause for the issues with city funding? |
| Learner Answer	|	 tax base |
| Correct Answer   	|	 ['much of the citys tax base dissipated', 'tax base dissipated'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output is a gramatically invalid answer to the question. |
 
| Context   	|	 Under the Scotland Act 1998, ordinary general elections for the Scottish Parliament are held on the first Thursday in May every four years (1999, 2003, 2007 and so on). The date of the poll may be varied by up to one month either way by the Monarch on the proposal of the Presiding Officer. If the Parliament itself resolves that it should be dissolved (with at least two-thirds of the Members voting in favour), or if the Parliament fails to nominate one of its members to be First Minister within 28 days of a General Election or of the position becoming vacant, the Presiding Officer proposes a date for an extraordinary general election and the Parliament is dissolved by the Queen by royal proclamation. Extraordinary general elections are in addition to ordinary general elections, unless held less than six months before the due date of an ordinary general election, in which case they supplant it. The following ordinary election reverts to the first Thursday in May, a multiple of four years after 1999 (i.e., 5 May 2011, 7 May 2015, etc.). |
| Question  	|	 What month, every four years, are the ordinary general elections held on? |
| Learner Answer	|	 thursday in may |
| Correct Answer   	|	 ['may', 'may', 'may'] |
| Correctness	|	 Incorrect |
| Reason    	|	 The model output is a month, while the question asks for a year. |
 
| Context   	|	 The Richard B. Russell National School Lunch Act  (79 P.L. 396, 60 Stat. 230) is a United States federal law that created the National School Lunch Program  (NSLP) to provide low - cost or free school lunch meals to qualified students through subsidies to schools. The program was established as a way to prop up food prices by absorbing farm surpluses, while at the same time providing food to school age children. It was named after Richard Russell, Jr., signed into law by President Harry S. Truman in 1946, and entered the federal government into schools dietary programs on June 4, 1946.  |
| Question  	|	 when did the free school lunch program start |
| Learner Answer	|	 1946 |
| Correct Answer   	|	 ['june 4 1946'] |
| Correctness	|	 Correct |
| Reason    	|	  |

| Context   	|	 "Let's Get It Started " is a song by American group The Black Eyed Peas, released as a single on June 22, 2004. The track was the fourth single released from the band's 2003 album Elephunk and is a re-worked version of the album's third track "Let's Get Retarded ". This version was included as a bonus track on the 2004 re-issue of the album.  |
| Question  	|	 who sings the song let's get it started in here |
| Learner Answer	|	 black eyed peas |
| Correct Answer   	|	 ['american group the black eyed peas'] |
| Correctness	|	 Correct |
| Reason    	|	 Black Eyed Peas is a specific enough name to point to one group |
 
| Context   	|	 Leviathan  (/ lɪˈvaɪ. əθən /; Hebrew: לִוְיָתָן, Modern Livyatan, Tiberian Liwyāṯān) is a sea monster referenced in the Hebrew Bible in the Book of Job, Psalms, and Isaiah.  |
| Question  	|	 where does it talk about leviathan in the bible |
| Learner Answer	|	 book of job psalms and isaiah |
| Correct Answer   	|	 ['book of job', 'psalms', 'isaiah'] |
| Correctness	|	 Correct |
| Reason    	|	 The model got all possible answers in list form |
 
| Context   	|	 King Belshazzar holds a great feast for a thousand of his lords, and commands that the Temple vessels from Jerusalem be brought in so that they can drink from them, but as the Babylonians drink, a hand appears and writes on the wall. Belshazzar calls for his magicians and diviners to interpret the writing, but they are unable even to read them. The queen advises Belshazzar to send for Daniel, renowned for his wisdom. Daniel is brought in, and the king offers to make him third in rank in the kingdom if he can interpret the writing. Daniel declines the honour, but agrees to the request. He reminds Belshazzar that Nebuchadnezzar's greatness was the gift of God, and that when he became arrogant God threw him down until he learned humility: "the Most High God has sovereignty over the kingdom of mortals, and sets over it whomever He will. " Belshazzar has drunk from the vessels of God's Temple and praised his idols, but he has not given honour to God, and so God sent this hand and wrote these words:  |
| Question  	|	 which king saw the writing on the wall |
| Learner Answer	|	 king belshazzar |
| Correct Answer   	|	 ['belshazzar'] |
| Correctness	|	 Correct |
| Reason    	|	  |

| Context   	|	 The 2018 PGA Championship was the 100th PGA Championship, held on August 9 -- 12 at Bellerive Country Club in Town and Country, Missouri, a suburb west of St. Louis. This was the second PGA Championship  (1992) and third major  (1965 U.S. Open) held at Bellerive. It was also the last to be held in the month of August. Just before the 2017 tournament, the PGA announced that the Championship will move to May in 2019.  |
| Question  	|	 where's the pga championship being played this weekend |
| Learner Answer	|	 bellerive country club |
| Correct Answer   	|	 ['at bellerive country club in town and country missouri a suburb west of st louis'] |
| Correctness	|	 Correct |
| Reason    	|	 Bellerive Country Club is a specific enough name to point to one place |
 
| Context   	|	 The brain structures that compose the reward system are located primarily within the cortico - basal ganglia - thalamo - cortical loop; the basal ganglia portion of the loop drives activity within the reward system. Most of the pathways that connect structures within the reward system are glutamatergic interneurons, GABAergic medium spiny neurons, and dopaminergic projection neurons, although other types of projection neurons contribute  (e.g., orexinergic projection neurons). The reward system includes the ventral tegmental area, ventral striatum  (i.e., the nucleus accumbens and olfactory tubercle), dorsal striatum  (i.e., the caudate nucleus and putamen), substantia nigra  (i.e., the pars compacta and pars reticulata), prefrontal cortex, anterior cingulate cortex, insular cortex, hippocampus, hypothalamus  (particularly, the orexinergic nucleus in the lateral hypothalamus), thalamus  (multiple nuclei), subthalamic nucleus, globus pallidus  (both external and internal), ventral pallidum, parabrachial nucleus, amygdala, and the remainder of the extended amygdala. The dorsal raphe nucleus and cerebellum appear to modulate some forms of reward - related cognition  (i.e., associative learning, motivational salience, and positive emotions) and behaviors as well.  |
| Question  	|	 where is the pleasure/reward center located in our brain |
| Learner Answer	|	 basal ganglia thalamo cortical loop |
| Correct Answer   	|	 ['primarily within the cortico basal ganglia thalamo cortical loop'] |
| Correctness	|	 Correct |
| Reason    	|	 This is an acceptable level of nuance |
 
| Context   	|	  Zeroth law of thermodynamics: If two systems are in thermal equilibrium with a third system, they are in thermal equilibrium with each other. This law helps define the concept of temperature.   First law of thermodynamics: When energy passes, as work, as heat, or with matter, into or out from a system, the system's internal energy changes in accord with the law of conservation of energy. Equivalently, perpetual motion machines of the first kind  (machines that produce work with no energy input) are impossible.   Second law of thermodynamics: In a natural thermodynamic process, the sum of the entropies of the interacting thermodynamic systems increases. Equivalently, perpetual motion machines of the second kind  (machines that spontaneously convert thermal energy into mechanical work) are impossible.   Third law of thermodynamics: The entropy of a system approaches a constant value as the temperature approaches absolute zero. With the exception of non-crystalline solids  (glasses) the entropy of a system at absolute zero is typically close to zero, and is equal to the natural logarithm of the product of the quantum ground states.   |
| Question  	|	 which law of thermodynamics is based on the conservation of energy law |
| Learner Answer	|	 first law |
| Correct Answer   	|	 ['first law of thermodynamics'] |
| Correctness	|	 Correct |
| Reason    	|	 If the question had instead only asked "What law is the energy conservation law" then this would be an incorrect answer, because it does not mention thermodynamics |