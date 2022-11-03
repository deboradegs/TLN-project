## Esercitazione #6 - "Let'splay" - False Friends

### Corpus
Il corpus è composto da un file (`text_emotion.csv`) contente 40000 tweet su svariati argomenti, preso dal progetto https://github.com/ragesh2000/Emotion-detection , resi un testo solo. Abbiamo scelto un corpus così vasto e vario poiché negli altri che abbiamo provato era difficile trovare parole identiche ma usate con diversi significati, se non impossibile.

### Idea
Per trovare gli omonimi in un testo abbiamo pensato di usare la libreria lesk, che è in grado di disambiguare una parola dato il contesto in cui è inserita. Inoltre restituisce, grazie al metodo definition(), la definizione del concetto che è stato disambiguato. A questo punto abbiamo creato un dataframe di parole che avessero più di una definizione in tutto il testo con le relative definizioni, e le chiavi di questo dataframe sono i nostri omonimi, o false friends.
```
pie             dish baked in pastry-lined pan often with a pastry top                                                                                             
                                                                                      a prehistoric unrecorded language that was the ancestor of all Indo-European languages
piece           a separate part of a whole                                                                                                                         
                                                                                      to join or unite the pieces of
pillow          rest on or as if on a pillow                                                                                                                       
                                                                                      a cushion to support the head of a sleeping person
pin             flagpole used to mark the position of the hole on a golf green                                                                                     
                                                                                      attach or fasten with pins or as if with pins; .
pineapple       a tropical American plant bearing a large fleshy edible fruit with a terminal tuft of stiff leaves; widely cultivated in the tropics               
                                                                                      large sweet fleshy tropical fruit with a terminal tuft of stiff leaves; widely cultivated
pirate          copy illegally; of published material                                                                                                              
                                                                                      someone who uses another person's words or ideas as if they were his own     
pit             the hard inner (usually woody) layer of the pericarp of some fruits (as peaches or plums or cherries or olives) that contains the seed             
                                                                                      remove the pits from
plan            make or work out a plan for; devise                                                                                                                
                                                                                      a series of steps to be carried out or goals to be accomplished              
                                                                                                                                                                   
                                                                                                                          have the will and intention to carry out some action
plane           make even or smooth, with or as with a carpenter's plane                                                                                           
                                                                                      an aircraft that has a fixed wing and is powered by propellers or jets       
plant           place something or someone in a certain position in order to secretly observe or deceive                                                           
                                                                                      put firmly in the mind
plate           (baseball) base consisting of a rubber slab where the batter stands; it must be touched by a base runner in order to score                         
                                                                                      a flat sheet of metal or glass on which a photographic image can be recorded 
play            (in games or plays or other performances) the time during which play proceeds                                                                      
                                                                                      a weak and tremulous light
player          a person who participates in or is skilled at some game                                                                                            
                                                                                      an important participant (as in a business deal)
plot            devise the sequence of events in (a literary work or a play, movie, or ballet)                                                                     
                                                                                      the story that is told in a novel or play or movie etc.
plus            on the positive side or higher end of a scale                                                                                                      
                                                                                      a useful or valuable quality
pocket          put in one's pocket                                                                                                                                
                                                                                      a hollow concave shape made by removing something
point           give a point to                                                                                                                                    
                                                                                      mark (a psalm text) to indicate the points at which the music changes        
poke            hit hard with the hand, fist, or some heavy instrument                                                                                             
                                                                                      a bag made of paper or plastic for holding customer's purchases
pool            join or form a pool of people                                                                                                                      
                                                                                      an organization of people or resources that can be shared
pop             music of general appeal to teenagers; a bland watered-down version of rock'n'roll with more rhythm and harmony and an emphasis on romantic love                                                                                          drink down entirely
post            place so as to be noticed                                                                                                                          
                                                                                      enter on a public list
poster          a horse kept at an inn or post house for use by mail carriers or for rent to travelers                                                             
                                                                                      a sign posted in a public place as an advertisement
posting         place so as to be noticed                                                                                                                          
                                                                                      assign to a station
pot             plant in a pot                                                                                                                                     
                                                                                      a plumbing fixture for defecation and urination
pound           a symbol for a unit of currency (especially for the pound sterling in Great Britain)                                                               
                                                                                      hit hard with the hand, fist, or some heavy instrument
pout            make a sad face and thrust out one's lower lip                                                                                                     
                                                                                      be in a huff and display one's displeasure
power           supply the force or power for the functioning of                                                                                                   
                                                                                      a state powerful enough to influence events throughout the world
pr              a promotion intended to create goodwill for a person or institution                                                                                
                                                                                      a self-governing commonwealth associated with the United States occupying the island of Puerto Rico
practice        engage in a rehearsal (of)                                                                                                                         
                                                                                      the exercise of a profession
prayer          someone who prays to God                                                                                                                           
                                                                                      a fixed text used in praying
premier         the person who holds the position of head of the government in the United Kingdom                                                                  
                                                                                      perform a work for the first time
preparation     the activity of putting or setting in order in advance of some act or purpose                                                                      
                                                                                      activity leading to skilled behavior
prescription    written instructions for an optician on the lenses for a given person                                                                              
                                                                                      a drug that is available only with written instructions from a doctor or dentist to a pharmacist
present         present somebody with something, usually to accuse or criticize                                                                                    
                                                                                      a verb tense that expresses actions or states at the time of speaking        
pressure        the force applied to a unit area of surface; measured in pascals (SI unit) or in dynes (cgs unit)                                                  
                                                                                      the somatic sensation that results from applying force to an area of skin    
preview         an advertisement consisting of short scenes from a motion picture that will appear in the near future                                              
                                                                                      watch (a movie or play) before it is released to the general public
price           ascertain or learn the price of                                                                                                                    
                                                                                      a monetary reward for helping to catch a criminal
priest          a person who performs religious duties and ceremonies in a non-Christian religion                                                                  
                                                                                      a clergyman in Christian churches who has the authority to perform or administer various religious rites; one of the Holy Orders
print           make into a print                                                                                                                                  
                                                                                      the text appearing in a book, newspaper, or other printed publication        
prize           to move or force, especially in an effort to get something open; :                                                                                 
                                                                                      something given for victory or superiority in a contest or competition or for winning a lottery
pro             in favor of a proposition, opinion, etc.                                                                                                           
                                                                                      an athlete who plays for pay
process         subject to a process or treatment, with the aim of readying for some purpose, improving, or remedying a condition                                  
                                                                                      a writ issued by authority of law; usually compels the defendant's attendance in a civil suit; failure to appear results in a default judgment against the defendant
produce         cause to happen, occur or exist                                                                                                                    
                                                                                      fresh fruits and vegetable grown for the market
producer        something that produces                                                                                                                            
                                                                                      someone who finds financing for and supervises the making and presentation of a show (play or film or program or similar work)
product         a consequence of someone's efforts or of a particular set of circumstances                                                                         
                                                                                      an artifact that has been created by someone or some process
prof            someone who is a member of the faculty at a college or university                                                                                  
                                                                                      provide evidence for
professional    a person engaged in one of the learned professions                                                                                                 
                                                                                      an athlete who plays for pay
project         extend out or project in space                                                                                                                     
                                                                                      cause to be heard
promise         promise to undertake or give                                                                                                                       
                                                                                      a verbal commitment by one person to another agreeing to do (or not to do) something in the future
prop            any movable articles or objects used on the set of a play or movie                                                                                 
                                                                                      a support placed beneath or against something to keep it from shaking or falling
provider        someone who provides the means for subsistence                                                                                                     
                                                                                      someone whose business is to supply a particular service or commodity        
puddle          wade or dabble in a puddle                                                                                                                         
                                                                                      mess around, as in a liquid or paste
pump            raise (gases or fluids) with a pump                                                                                                                
                                                                                      supply in great quantities
pup             young of any of various canines such as a dog or wolf                                                                                              
                                                                                      birth
puppy           a young dog                                                                                                                                        
                                                                                      an inexperienced young person
purchase        a means of exerting influence or gaining advantage                                                                                                 
                                                                                      the acquisition of something for payment
purpose         the quality of being determined to do or achieve something; firmness of purpose                                                                    
                                                                                      what something is used for
put             the option to sell a given stock (or stock index or commodity future) at a given price before a given date                                         
                                                                                      cause to be in a certain state; cause to be in a certain relation
puzzle          a game that tests your ingenuity                                                                                                                   
                                                                                      be uncertain about; think about without fully understanding or being able to decide
question        pose a question                                                                                                                                    
                                                                                      pose a series of questions to
quid            something for something; that which a party receives (or is promised) in return for something he does or gives or promises                         
                                                                                      a wad of something chewable as tobacco
quote           a punctuation mark used to attribute the enclosed text to someone else                                                                             
                                                                                      name the price of                                                            
                                                                                                                                                                   
                                                                                                                          put quote marks around
r               the length of a line segment between the center and circumference of a circle or sphere                                                            
                                                                                      a unit of radiation exposure; the dose of ionizing radiation that will produce 1 electrostatic unit of electricity in 1 cc of dry air
rabbit          the fur of a rabbit                                                                                                                                
                                                                                      any of various burrowing animals of the family Leporidae having long ears and short tails; some domesticated and raised for pets or food
race            cause to move fast or to rush or race                                                                                                              
                                                                                      people who are believed to belong to the same genetic stock
raffle          a lottery in which the prizes are goods rather than money                                                                                          
                                                                                      British colonial administrator who founded Singapore (1781-1826)
raid            an attempt by speculators to defraud investors                                                                                                     
                                                                                      search for something needed or desired
raise           collect funds for a specific purpose                                                                                                               
                                                                                      bring (a surface or a design) into relief and cause to project
ranger          a member of the Texas state highway patrol; formerly a mounted lawman who maintained order on the frontier                                         
                                                                                      an official who is responsible for managing and protecting an area of forest 
rap             genre of African-American music of the 1980s and 1990s in which rhyming lyrics are chanted to a musical accompaniment; several forms of rap have emerged                                                                                 make light, repeated taps on a surface
rape            force (someone) to have sex against their will                                                                                                     
                                                                                      the crime of forcing a woman to submit to sexual intercourse against her will
rat             a person who is deemed to be despicable or contemptible                                                                                            
                                                                                      give (hair) the appearance of being fuller by using a rat
rate            estimate the value of                                                                                                                              
                                                                                      a local tax on property (usually used in the plural)
ray             the syllable naming the second (supertonic) note of any major scale in solmization                                                                 
                                                                                      any of the stiff bony spines in the fin of a fish
reach           reach a goal, e.g.,                                                                                                                                
                                                                                      the limits within which something can be effective
reaction        (mechanics) the equal and opposite force that is produced when any force is applied to a body                                                      
                                                                                      doing something in opposition to another way of doing it that you don't like 
read            to hear and understand                                                                                                                             
                                                                                      interpret something in a certain way; convey a particular meaning or impression
real            coinciding with reality; - F.A.Olafson                                                                                                             
                                                                                      any rational or irrational number
rear            located in or toward the back or rear                                                                                                              
                                                                                      the side of an object that is opposite its front
reason          decide by reasoning; draw or come to a conclusion                                                                                                  
                                                                                      the state of having good sense and sound judgment
receipt         report the receipt of                                                                                                                              
                                                                                      the entire amount of income before any deductions are made
reception       the manner in which something is greeted                                                                                                           
                                                                                      (American football) the act of catching a pass in football
record          make a record of; set down in permanent form                                                                                                       
                                                                                      a list of crimes for which an accused person has been previously convicted   
recording       a storage device on which information (sounds or images) have been recorded                                                                        
                                                                                      the act of making a record (especially an audio record)
red             red color or pigment; the chromatic color resembling the hue of blood                                                                              
                                                                                      a tributary of the Mississippi River that flows eastward from Texas along the southern boundary of Oklahoma and through Louisiana
reef            a rocky region in the southern Transvaal in northeastern South Africa; contains rich gold deposits and coal and manganese                          
                                                                                      one of several strips across a sail that can be taken in or rolled up to lessen the area of the sail that is exposed to the wind
reference       the relation between a word or phrase and the object or idea it refers to                                                                          
                                                                                      a book to which you can refer for authoritative facts
region          a knowledge domain that you are interested in or are communicating about                                                                           
                                                                                      a large indefinite location on the surface of the Earth
regret          express with regret                                                                                                                                
                                                                                      feel sad about the loss or absence of
reject          reject with contempt                                                                                                                               
                                                                                      dismiss from consideration or a contest
relay           electrical device such that current flowing through it in one circuit can switch on and off a current in a second circuit                          
                                                                                      control or operate by relay
release         the act of allowing a fluid to escape                                                                                                              
                                                                                      the termination of someone's employment (leaving them free to depart)        
remedy          provide relief for                                                                                                                                 
                                                                                      a medicine or therapy that cures disease or relieve pain
rent            a payment or series of payments made by the lessee to an owner for use of some property, facility, equipment, or service                           
                                                                                      hold under a lease or rental agreement; of goods and services
replacement     a person or thing that takes or can take the place of another                                                                                      
                                                                                      someone who takes the place of another person
reply           a statement (either spoken or written) that is made to reply to a question or request or criticism or accusation                                   
                                                                                      the speech act of continuing a conversational exchange
representative  being or characteristic of government by representation in which citizens exercise power through elected officers and representatives              
                                                                                      a member of the United States House of Representatives
request         a formal message requesting something that is submitted to an authority                                                                            
                                                                                      inquire for (information)
rerun           rerun a performance of a play, for example                                                                                                         
                                                                                      cause to perform again
reservation     a district that is reserved for particular purpose                                                                                                 
                                                                                      the act of keeping back or setting aside for some future occasion
reserve         arrange for and reserve (something for someone else) in advance                                                                                    
                                                                                      armed forces that are not on active duty but can be called in an emergency   
respect         show respect towards                                                                                                                               
                                                                                      behavior intended to please your parents
restriction     a principle that limits the extent of something                                                                                                    
                                                                                      the act of keeping something within specified bounds (by force if necessary) 
result          a statement that solves a problem or explains how to solve the problem                                                                             
                                                                                      something that results
resume          give a summary (of)                                                                                                                                
                                                                                      return to a previous location or condition
retainer        a person working in the service of another (especially in the household)                                                                           
                                                                                      a dental appliance that holds teeth (or a prosthesis) in position after orthodontic treatment
return          the key on electric typewriters or computer keyboards that causes a carriage return and a line feed                                                
                                                                                      the act of going back to a prior location
reunion         a party of former associates who have come together again                                                                                          
                                                                                      the act of coming together again
review          hold a review (of troops)                                                                                                                          
                                                                                      (accounting) a service (less exhaustive than an audit) that provides some assurance to interested parties as to the reliability of financial data
reward          a recompense for worthy acts or retribution for wrongdoing                                                                                         
                                                                                      the offer of money for helping to find a criminal or for returning lost property
ride            a mechanical device that you ride for amusement or excitement                                                                                      
                                                                                      keep partially engaged by slightly depressing a pedal with the foot
right           the hand that is on the right side of the body                                                                                                     
                                                                                      the piece of ground in the outfield on the catcher's right
ring            attach a ring to the foot of, in order to identify                                                                                                 
                                                                                      make (bells) ring, often for the purposes of musical edification
risk            take a risk in the hope of a favorable outcome                                                                                                     
                                                                                      expose to a chance of loss or damage
rock            cause to move back and forth                                                                                                                       
                                                                                      hard bright-colored stick candy (typically flavored with peppermint)
rocket          shoot up abruptly, like a rocket                                                                                                                   
                                                                                      propels bright light high in the sky, or used to propel a lifesaving line or harpoon
room            the people who are present in a room                                                                                                               
                                                                                      apartment consisting of a series of connected rooms used as a living unit (as in a hotel)
roomy           an associate who shares a room with you                                                                                                            
                                                                                      (of buildings and rooms) having ample space
root            take root and begin to grow                                                                                                                        
                                                                                      become settled or established and stable in one's residence or life style    
rose            of something having a dusty purplish pink color                                                                                                    
                                                                                      any of many shrubs of the genus Rosa that bear roses
routine         a short theatrical performance that is part of a longer program                                                                                    
                                                                                      a set sequence of steps, part of larger computer program
row             an arrangement of objects or people side by side in a line                                                                                         
                                                                                      the act of rowing as a sport
ruby            of a color at the end of the color spectrum (next to orange); resembling the color of blood or cherries or tomatoes or rubies                      
                                                                                      a transparent piece of ruby that has been cut and polished and is valued as a precious gem
ruin            fall into ruin                                                                                                                                     
                                                                                      reduce to ruins
rule            (linguistics) a rule describing (or prescribing) a linguistic practice                                                                             
                                                                                      directions that define the way a game or sport is to be conducted
rumour          gossip (usually a mixture of truth and untruth) passed around by word of mouth                                                                     
                                                                                      tell or spread rumors
run             run with the ball; in such sports as football                                                                                                      
                                                                                      have a tendency or disposition to do or be something; be inclined
runner          a baseball player on the team at bat who is on base (or attempting to reach a base)                                                                
                                                                                      a horizontal branch from the base of plant that produces new plants from buds at its tips
s               an abundant tasteless odorless multivalent nonmetallic element; best known in yellow crystals; occurs in many sulphide and sulphate minerals and even in native form (especially in volcanic regions)                                    the United States intelligence agency that protects current and former presidents and vice presidents and their immediate families and protects distinguished foreign visitors; detects and apprehends counterfeiters; suppresses forgery of government securities and documents
saint           a person who has died and has been declared a saint by canonization                                                                                
                                                                                      declare (a dead person) to be a saint
sale            an agreement (or contract) in which property is transferred from the seller (vendor) to the buyer (vendee) for a fixed price in money (paid or agreed to be paid by the buyer)                                                           income (at invoice values) received for goods and services over some given period of time
salt            the taste experience when common salt is taken into the mouth                                                                                      
                                                                                      negotiations between the United States and the Union of Soviet Socialist Republics opened in 1969 in Helsinki designed to limit both countries' stock of nuclear weapons
sand            a loose material consisting of grains of rock or coral                                                                                             
                                                                                      rub with sandpaper
sandwich        make into a sandwich                                                                                                                               
                                                                                      insert or squeeze tightly between two people or objects
sat             serve in a specific professional capacity                                                                                                          
                                                                                      the seventh and last day of the week; observed as the Sabbath by Jews and some Christians
sausage         a small nonrigid airship used for observation or as a barrage balloon                                                                              
                                                                                      highly seasoned minced meat stuffed in casings
save            record data on a computer                                                                                                                          
                                                                                      spend sparingly, avoid the waste of
saying          a word or phrase that particular people use in particular situations                                                                               
                                                                                      give instructions to or direct somebody to do something with authority       
sb              a metallic element having four allotropic forms; used in a wide variety of alloys; found in stibnite                                               
                                                                                      a bachelor's degree in science
scale           size or measure according to a scale                                                                                                               
                                                                                      remove the scales from
scene           the visual percept of a region                                                                                                                     
                                                                                      the context and environment in which something is set
school          educate in or as if in a school                                                                                                                    
                                                                                      teach or refine to be discriminative in taste or judgment
score           write a musical score for                                                                                                                          
                                                                                      induce to have sex
scratch         remove by erasing or crossing out or as if by drawing a line                                                                                       
                                                                                      a competitor who has withdrawn from competition
scratching      remove by erasing or crossing out or as if by drawing a line                                                                                       
                                                                                      cut the surface of; wear away the surface of
screen          project onto a screen for viewing                                                                                                                  
                                                                                      the display that is electronically created on the surface of the large end of a cathode-ray tube
screening       the display of a motion picture                                                                                                                    
                                                                                      testing objects or persons in order to identify those with particular characteristics
screw           turn like a screw                                                                                                                                  
                                                                                      have sexual intercourse with
sealer          an official who affixes a seal to a document                                                                                                       
                                                                                      a kind of sealing material that is used to form a hard coating on a porous surface (as a coat of paint or varnish used to size a surface)
search          subject to a search                                                                                                                                
                                                                                      an operation that determines whether one or more of a set of items has a specified property
seat            place in or on a seat                                                                                                                              
                                                                                      provide with seats
secret          having an import not apparent to the senses nor obvious to the intelligence; beyond ordinary understanding                                         
                                                                                      information known only to a special group
section         a land unit equal to 1 square mile                                                                                                                 
                                                                                      a small class of students who are part of a larger course but are taught separately
see             go to see a place, as for entertainment                                                                                                            
                                                                                      see and understand, have a good eye
self            (used as a combining form) relating to--of or by or to or from or for--the self                                                                    
                                                                                      your consciousness of your own identity
sell            be sold at a certain price or in a certain way                                                                                                     
                                                                                      the activity of persuading someone to buy
semi            a trailer having wheels only in the rear; the front is supported by the towing vehicle                                                             
                                                                                      a truck consisting of a tractor and trailer together
seminar         any meeting for an exchange of ideas                                                                                                               
                                                                                      a course offered for a small group of advanced students
senior          used of the fourth and final year in United States high school or college                                                                          
                                                                                      an undergraduate student during the year preceding graduation
sent            transport commercially                                                                                                                             
                                                                                      100 senti equal 1 kroon in Estonia
sentiment       a personal belief or judgment that is not founded on proof or certainty                                                                            
                                                                                      tender, romantic, or nostalgic feeling or emotion
separate        standing apart; not attached to or supported by anything                                                                                           
                                                                                      discontinue an association or relation; go different ways
sermon          an address of a religious nature (usually delivered during a church service)                                                                       
                                                                                      a moralistic rebuke
server          (computer science) a computer that provides client stations with access to files and printers as shared resources to a computer network            
                                                                                      a person whose occupation is to serve at table (as in a restaurant)
service         (law) the acts performed by an English feudal tenant for the benefit of his lord which formed the consideration for the property granted to him                                                                                          performance of duties or provision of space and equipment helpful to others  
set             set in type                                                                                                                                        
                                                                                      evil Egyptian god with the head of a beast that has high square ears and a long snout; brother and murderer of Osiris
seven           one of four playing cards in a deck with seven pips on the face                                                                                    
                                                                                      a card game in which you play your sevens and other cards in sequence in the same suit as the sevens; you win if you are the first to use all your cards
shade           represent the effect of shade or shadow on                                                                                                         
                                                                                      spectacles that are darkened or polarized to protect the eyes from the glare of the sun
shake           shake (a body part) to communicate a greeting, feeling, or cognitive state                                                                         
                                                                                      causing to move repeatedly from side to side
share           give out as one's portion or share                                                                                                                 
                                                                                      have in common
shelf           a projecting ridge on a mountain or submerged under water                                                                                          
                                                                                      place on a shelf
shell           remove from its shell or outer covering                                                                                                            
                                                                                      look for and collect shells by the seashore
shift           (geology) a crack in the earth's crust resulting from the displacement of one side with respect to the other                                       
                                                                                      an event in which something is displaced without rotation
shin            the inner and thicker of the two bones of the human leg between the knee and ankle                                                                 
                                                                                      a cut of meat from the lower part of the leg
shine           be clear and obvious                                                                                                                               
                                                                                      throw or flash the light of (a lamp)
shirt           put a shirt on                                                                                                                                     
                                                                                      a garment worn on the upper half of the body
shit            something of little value                                                                                                                          
                                                                                      insulting terms of address for people who are stupid or irritating or ridiculous
shoe            furnish with shoes                                                                                                                                 
                                                                                      footwear shaped to fit the foot (below the ankle) with a flexible upper of leather or plastic and a sole and heel of heavier material
shoot           measure the altitude of by using a sextant                                                                                                         
                                                                                      record on photographic film
shooting        the act of firing a projectile                                                                                                                     
                                                                                      throw dice, as in a crap game
shop            a course of instruction in a trade (as carpentry or electricity)                                                                                   
                                                                                      a mercantile establishment for the retail sale of goods or services
short           so as to interrupt                                                                                                                                 
                                                                                      the fielding position of the player on a baseball team who is stationed between second and third base
shot            sports equipment consisting of a heavy metal ball used in the shot put                                                                             
                                                                                      an attempt to score in a game
shoulder        the part of a garment that covers or fits over the shoulder                                                                                        
                                                                                      push with the shoulders
shout           utter a sudden loud cry                                                                                                                            
                                                                                      utter in a loud voice; talk in a loud voice (usually denoting characteristic manner of speaking)
show            pretending that something is the case in order to make a good impression                                                                           
                                                                                      something intended to communicate a particular impression                    
                                                                                                                                                                   
                                                                                                                          the act of publicly exhibiting or entertaining
shuffle         move about, move back and forth                                                                                                                    
                                                                                      mix so as to make a random order or arrangement
si              the syllable naming the seventh (subtonic) note of any musical scale in solmization                                                                
                                                                                      a tetravalent nonmetallic element; next to oxygen it is the most abundant element in the earth's crust; occurs in clay and feldspar and granite and quartz and sand; used as a semiconductor in transistors
sight           the act of looking or seeing or observing                                                                                                          
                                                                                      catch sight of; to perceive with the eyes
sign            make the sign of the cross over someone in order to call on God for protection; consecrate                                                         
                                                                                      a fundamental linguistic unit linking a signifier to that which is signified; --de Saussure
signal          be a signal for or a symptom of                                                                                                                    
                                                                                      communicate silently and non-verbally by signals or signs
signing         make the sign of the cross over someone in order to call on God for protection; consecrate                                                         
                                                                                      communicate in sign language
sin             an act that is regarded by theologians as a transgression of God's will                                                                            
                                                                                      ratio of the length of the side opposite the given angle to the length of the hypotenuse of a right-angled triangle
singer          United States inventor of an improved chain-stitch sewing machine (1811-1875)                                                                      
                                                                                      United States writer (born in Poland) of Yiddish stories and novels (1904-1991)
sink            fall or sink heavily                                                                                                                               
                                                                                      a depression in the ground communicating with a subterranean passage (especially in limestone) and formed by solution or by collapse of a cavern roof
sister          (Roman Catholic Church) a title given to a nun (and used as a form of address)                                                                     
                                                                                      a female person who is a fellow member of a sorority or labor union or other group
situation       a condition or position in which you find yourself                                                                                                 
                                                                                      a complex or critical or unusual difficulty
size            the property resulting from being one of a series of graduated measurements (as of clothing)                                                       
                                                                                      cover or stiffen or glaze a porous material with size or sizing (a glutinous substance)
skate           large edible rays having a long snout and thick tail with pectoral fins continuous with the head; swim by undulating the edges of the pectoral fins                                                                                      move along on skates
sketch          make a sketch of                                                                                                                                   
                                                                                      describe roughly or briefly or give the main points or summary of
skill           an ability that has been acquired by training                                                                                                      
                                                                                      ability to produce solutions in some problem domain
skin            bruise, cut, or injure the skin or the surface of                                                                                                  
                                                                                      a bag serving as a container for liquids; it is made from the hide of an animal
skip            cause to skip over a surface                                                                                                                       
                                                                                      a gait in which steps and hops alternate
skirt           a garment hanging from the waist; worn mainly by girls and women                                                                                   
                                                                                      cloth covering that forms the part of a garment below the waist
sleep           euphemisms for death (based on an analogy between lying in a bed and in a tomb)                                                                    
                                                                                      a natural and periodic state of rest during which consciousness of the world is suspended
sleeve          small case into which an object fits                                                                                                               
                                                                                      the part of a garment that is attached at the armhole and that provides a cloth covering for the arm
slide           a transparency mounted in a frame; viewed with a slide projector                                                                                   
                                                                                      (music) rapid sliding up or down the musical scale
slip            artifact consisting of a narrow flat piece of material                                                                                             
                                                                                      cause to move with a smooth or sliding motion
slot            assign a time slot                                                                                                                                 
                                                                                      a time assigned on a schedule or agenda
smack           deliver a hard blow to                                                                                                                             
                                                                                      press (the lips) together and open (the lips) noisily, as in eating
smoke           inhale and exhale smoke from cigarettes, cigars, pipes                                                                                             
                                                                                      the act of smoking tobacco or other substances
smoothy         a thick smooth drink consisting of fresh fruit pureed with ice cream or yoghurt or milk                                                            
                                                                                      someone with an assured and ingratiating manner
smut            affect with smut or mildew, as of a crop such as corn                                                                                              
                                                                                      any fungus of the order Ustilaginales
snake           move smoothly and sinuously, like a snake                                                                                                          
                                                                                      something long, thin, and flexible that resembles a snake
snap            tender green beans without strings that easily snap into sections                                                                                  
                                                                                      the act of snapping the fingers; movement of a finger from the tip to the base of the thumb on the same hand
sneak           marked by quiet and caution and secrecy; taking pains to avoid being observed                                                                      
                                                                                      put, bring, or take in a secretive or furtive manner
sneeze          a symptom consisting of the involuntary expulsion of air from the nose                                                                             
                                                                                      exhale spasmodically, as when an irritant entered one's nose
snicker         laugh quietly                                                                                                                                      
                                                                                      a disrespectful laugh
snot            nasal mucus                                                                                                                                        
                                                                                      a person regarded as arrogant and annoying
so              in the way indicated; ; ; (`thusly' is a nonstandard variant)                                                                                      
                                                                                      an internationally recognized distress signal in radio code
soap            rub soap all over, usually with the purpose of cleaning                                                                                            
                                                                                      money offered as a bribe
solution        a method for solving a problem                                                                                                                     
                                                                                      the successful action of solving a problem
son             a male human offspring                                                                                                                             
                                                                                      the divine word of God; the second person in the Trinity (incarnate in Jesus)
sorrow          sadness associated with some wrong done or some disappointment                                                                                     
                                                                                      the state of being sad
sort            an operation that segregates items into groups according to a specified criterion                                                                  
                                                                                      a person of a particular character or nature
sound           cause to sound                                                                                                                                     
                                                                                      give off a certain sound or sounds
source          (technology) a process by which energy or a substance enters a system                                                                              
                                                                                      specify the origin of
space           a blank character used to separate successive words in writing or printing                                                                         
                                                                                      one of the areas between or below or above the lines of a musical staff      
spare           an extra car wheel and tire for a four-wheel vehicle                                                                                               
                                                                                      an extra component of a machine or other apparatus
spark           a small but noticeable trace of some quality that might become stronger                                                                            
                                                                                      emit or produce sparks
speaker         electro-acoustic transducer that converts electrical signals into sounds loud enough to be heard at a distance                                     
                                                                                      the presiding officer of a deliberative assembly
spec            a detailed description of design criteria for a piece of work                                                                                      
                                                                                      optical instrument consisting of a frame that holds a pair of lenses for correcting defective vision
special         a special offering (usually temporary and at a reduced price) that is featured in advertising                                                      
                                                                                      a television production that features a particular person or work or topic   
speech          the act of delivering a formal spoken communication to an audience                                                                                 
                                                                                      the exchange of spoken words
speed           a central nervous system stimulant that increases energy and decreases appetite; used to treat narcolepsy and some forms of depression             
                                                                                      move very fast
spell           place under a spell                                                                                                                                
                                                                                      write or name the letters that comprise the conventionally accepted form of (a word or part of a word)
spike           bring forth a spike or spikes                                                                                                                      
                                                                                      sports equipment consisting of a sharp point on the sole of a shoe worn by athletes
spit            expel or eject (saliva or phlegm or sputum) from the mouth                                                                                         
                                                                                      a skewer for holding meat over a fire
spoiler         a candidate with no chance of winning but who may draw enough votes to prevent one of the leading candidates from winning                          
                                                                                      a hinged airfoil on the upper surface of an aircraft wing that is raised to reduce lift and increase drag
sport           wear or display in an ostentatious or proud manner                                                                                                 
                                                                                      someone who engages in sports
spot            mark with a spot or spots so as to allow easy recognition                                                                                          
                                                                                      spots before the eyes caused by opaque cell fragments in the vitreous humor and lens
spread          a tasty mixture to be spread on bread or crackers or used in preparing other dishes                                                                
                                                                                      the expansion of a person's girth (especially at middle age)
spring          the elasticity of something that can be stretched and returns to its original length                                                               
                                                                                      the season of growth
sprout          any new growth of a plant such as a new branch or a bud                                                                                            
                                                                                      put forth and grow sprouts or shoots
spur            strike with a spur                                                                                                                                 
                                                                                      tubular extension at the base of the corolla in some flowers
stack           a storage device that handles data so that the next item to be retrieved is the item most recently stored (LIFO)                                   
                                                                                      storage space in a library consisting of an extensive arrangement of bookshelves where most of the books are stored
stake           tie or fasten to a stake                                                                                                                           
                                                                                      a pole or stake set up to mark something (as the start or end of a race track)
stamp           affix a stamp to                                                                                                                                   
                                                                                      crush or grind with a heavy instrument
stand           have or maintain a position or stand on an issue                                                                                                   
                                                                                      the position where a thing or person stands
star            be the star in a performance                                                                                                                       
                                                                                      the topology of a network whose components are connected to a hub
start           a line indicating the location of the start of a race or a game                                                                                    
                                                                                      a turn to be a starter (in a game at the beginning)                          
                                                                                                                                                                   
                                                                                                                          the advantage gained by beginning early (as in a race)
state           a state of depression or agitation                                                                                                                 
                                                                                      (chemistry) the three traditional states of matter are solids (fixed shape and volume) and liquids (fixed volume and shaped by the container) and gases (filling the container)
statement       a document showing credits and debits                                                                                                              
                                                                                      (music) the presentation of a musical theme
station         the frequency assigned to a broadcasting station                                                                                                   
                                                                                      (Roman Catholic Church) a devotion consisting of fourteen prayers said before a series of fourteen pictures or carvings representing successive incidents during Jesus' passage from Pilate's house to his crucifixion at Calvary
stay            stay put (in a certain place)                                                                                                                      
                                                                                      fasten with stays
steal           take without the owner's consent                                                                                                                   
                                                                                      steal a base
step            place (a ship's mast) in its step                                                                                                                  
                                                                                      move or proceed as if by steps into a new situation
stereo          reproducer in which two microphones feed two or more loudspeakers to give a three-dimensional effect to the sound                                  
                                                                                      two photographs taken from slightly different angles that appear three-dimensional when viewed together
steroid         any hormone affecting the development and growth of sex organs                                                                                     
                                                                                      any of several fat-soluble organic compounds having as a basis 17 carbon atoms in four rings; many have important physiological effects
stick           a lever used by a pilot to control the ailerons and elevators of an airplane                                                                       
                                                                                      saddle with something disagreeable or disadvantageous
sting           deliver a sting to                                                                                                                                 
                                                                                      cause an emotional pain, as if by stinging
stink           be extremely bad in quality or in one's performance                                                                                                
                                                                                      a distinctive odor that is offensively unpleasant
stock           a certificate documenting the shareholder's ownership in the corporation                                                                           
                                                                                      a plant or stem onto which a graft is made; especially a plant grown specifically to provide the root part of grafted plants
stone           United States jurist who was named chief justice of the United States Supreme Court in 1941 by Franklin D. Roosevelt (1872-1946)                   
                                                                                      kill by throwing stones at
store           a depository for goods                                                                                                                             
                                                                                      a mercantile establishment for the retail sale of goods or services
story           a piece of fiction that narrates a chain of related events                                                                                         
                                                                                      a short account of the news
storm           a direct and violent assault on a stronghold                                                                                                       
                                                                                      attack by storm; attack suddenly
strawberry      any of various low perennial herbs with many runners and bearing white flowers followed by edible fruits having many small achenes scattered on the surface of an enlarged red pulpy berry                                               a soft red birthmark
stream          something that resembles a flowing stream in moving continuously                                                                                   
                                                                                      dominant course (suggestive of running water) of successive events or ideas  
street          the streets of a city viewed as a depressed environment in which there is poverty and crime and prostitution and dereliction                       
                                                                                      people living or working on the same street
stretch         extend or stretch out to a greater or the full length                                                                                              
                                                                                      an unbroken period of time during which you do something
strike          arrive at after reckoning, deliberating, and weighing                                                                                              
                                                                                      remove by erasing or crossing out or as if by drawing a line
string          string together; tie or fasten with a string                                                                                                       
                                                                                      provide with strings
strip           strip the cured leaves from                                                                                                                        
                                                                                      remove a constituent from a liquid
structure       give a structure to                                                                                                                                
                                                                                      the people in a society considered as a system organized by a characteristic pattern of relationships
struggle        be engaged in a fight; carry on a fight                                                                                                            
                                                                                      to exert strenuous effort against opposition
stuff           treat with grease, fill, and prepare for mounting                                                                                                  
                                                                                      press or force
style           make consistent with certain rules of style                                                                                                        
                                                                                      designate by an identifying term
sub             be a substitute                                                                                                                                    
                                                                                      a large sandwich made of a long crusty roll split lengthwise and filled with meats and cheese (and tomato and onion and lettuce and condiments); different names are used in different sections of the United States
subject         a person who is subjected to experimental or other observational procedures; someone who is an object of investigation                             
                                                                                      refer for judgment or consideration
suck            give suck to                                                                                                                                       
                                                                                      the act of sucking                                                           
                                                                                                                                                                   
                                                                                                                          draw something in by or as if by a vacuum                                                                                                     be inadequate or objectionable
sugar           sweeten with sugar                                                                                                                                 
                                                                                      an essential structural component of living cells and source of energy for animals; includes simple sugars with small molecules as well as macromolecular substances; are classified according to the number of monosaccharide groups they contain
suggestion      persuasion formulated as a suggestion                                                                                                              
                                                                                      a just detectable amount
suicide         a person who kills himself intentionally                                                                                                           
                                                                                      the act of killing yourself
suit            a petition or appeal made to a person of superior status or rank                                                                                   
                                                                                      playing card in any of four sets of 13 cards in a pack; each set has its own symbol and color
suite           a matching set of furniture                                                                                                                        
                                                                                      the group following and attending to some important person
sum             determine the sum of                                                                                                                               
                                                                                      a set containing all and only the members of two or more given sets
summer          spend the summer                                                                                                                                   
                                                                                      the warmest season of the year; in the northern hemisphere it extends from the summer solstice to the autumnal equinox
sun             the rays of the sun                                                                                                                                
                                                                                      the star that is the source of light and heat for the planets in the solar system
supply          the activity of supplying or providing something                                                                                                   
                                                                                      offering goods and services for sale
support         support materially or financially                                                                                                                  
                                                                                      a musical part (vocal or instrumental) that supports or provides background for other musical parts
supporter       a band (usually elastic) worn around the leg to hold up a stocking (or around the arm to hold up a sleeve)                                         
                                                                                      a support for the genitals worn by men engaging in strenuous exercise        
surprise        a sudden unexpected event                                                                                                                          
                                                                                      the act of surprising someone
sway            move or walk in a swinging or swaying manner                                                                                                       
                                                                                      cause to move back and forth
sweat           salty fluid secreted by sweat glands                                                                                                               
                                                                                      excrete perspiration through the pores in the skin
sweet           pleasing to the senses                                                                                                                             
                                                                                      the taste experience when sugar dissolves in the mouth
switch          cause to go on or to be engaged or set in operation                                                                                                
                                                                                      exchange or give (something) in exchange for
system          (physical chemistry) a sample of matter in which substances in different phases are in equilibrium                                                 
                                                                                      instrumentality that combines interrelated interacting artifacts designed to work as a coherent entity
tab             a short strip of material attached to or projecting from something in order to facilitate opening or identifying or handling it                    
                                                                                      a dose of medicine in the form of a small pellet
table           a company of people assembled at a table for a meal or game                                                                                        
                                                                                      a piece of furniture having a smooth flat top that is usually supported by one or more vertical legs
tag             a label associated with something for the purpose of identification                                                                                
                                                                                      touch a player while he is holding the ball
tail            any projection that resembles the tail of an animal                                                                                                
                                                                                      formalwear consisting of full evening dress for men
take            ascertain or determine by measuring, computing or take a reading from a dial                                                                       
                                                                                      be seized or affected in a specified way
tank            treat in a tank                                                                                                                                    
                                                                                      store in a tank by causing (something) to flow into it
tap             tap a telephone or telegraph wire to get information                                                                                               
                                                                                      make light, repeated taps on a surface
tape            fasten or attach with tape                                                                                                                         
                                                                                      tap a telephone or telegraph wire to get information
task            any piece of work that is undertaken or attempted                                                                                                  
                                                                                      use to the limit
taste           a kind of sensing; distinguishing substances by means of the taste buds                                                                            
                                                                                      the sensation that results when taste buds in the tongue and throat convey information about the chemical composition of a soluble stimulus
tattoo          stain (skin) with indelible color                                                                                                                  
                                                                                      the practice of making a design on the skin by pricking and staining
tax             levy a tax on                                                                                                                                      
                                                                                      charge against a citizen's person or property or activity for the support of government
te              the syllable naming the seventh (subtonic) note of any musical scale in solmization                                                                
                                                                                      a brittle silver-white metalloid element that is related to selenium and sulfur; it is used in alloys and as a semiconductor; occurs mainly as tellurides in ores of copper and nickel and silver and gold
team            two or more draft animals that work together to pull something                                                                                     
                                                                                      form a team
tear            fill with tears or shed tears                                                                                                                      
                                                                                      the process of shedding tears (usually accompanied by sobs or other inarticulate sounds)
tee             connect with a tee                                                                                                                                 
                                                                                      place on a tee
teen            a juvenile between the onset of puberty and maturity                                                                                               
                                                                                      all the numbers that end in -teen
tell            give instructions to or direct somebody to do something with authority                                                                             
                                                                                      a Swiss patriot who lived in the early 14th century and who was renowned for his skill as an archer; according to legend an Austrian governor compelled him to shoot an apple from his son's head with his crossbow (which he did successfully without mishap)
teller          United States physicist (born in Hungary) who worked on the first atom bomb and the first hydrogen bomb (1908-2003)                                
                                                                                      an official appointed to count the votes (especially in legislative assembly)
temple          the flat area on either side of the forehead                                                                                                       
                                                                                      an edifice devoted to special or exalted purposes
temptation      the desire to have or do something that you know you should avoid                                                                                  
                                                                                      the act of influencing by exciting hope or desire
tenor           (of a musical instrument) intermediate between alto and baritone or bass                                                                           
                                                                                      the general meaning or substance of an utterance
term            name formally or designate with a term                                                                                                             
                                                                                      (architecture) a statue or a human bust or an animal carved out of the top of a square pillar; originally used as a boundary marker in ancient Rome
terminal        relating to or occurring in a term or fixed period of time                                                                                         
                                                                                      a contact on an electrical device (such as a battery) at which electric current enters or leaves
test            test or examine for the presence of disease or infection                                                                                           
                                                                                      trying something to find out about it
text            a book prepared for use in schools or colleges                                                                                                     
                                                                                      the main body of a written work (as distinct from illustrations or footnotes etc.)
theater         a building where theatrical performances or motion-picture shows can be presented                                                                  
                                                                                      a region in which active military operations are in progress
theatre         a building where theatrical performances or motion-picture shows can be presented                                                                  
                                                                                      a region in which active military operations are in progress
there           to or toward that place; away from the speaker                                                                                                     
                                                                                      a location other than here; that place
thing           a persistent illogical feeling of desire or aversion                                                                                               
                                                                                      any movable possession (especially articles of clothing)
think           use or exercise the mind or one's power of reason in order to make inferences, decisions, or arrive at a solution or judgments                     
                                                                                      bring into a given condition by mental preoccupation
third           the third from the lowest forward ratio gear in the gear box of a motor vehicle                                                                    
                                                                                      the fielding position of the player on a baseball team who is stationed near the third of the bases in the infield (counting counterclockwise from home plate)
thought         be capable of conscious thought                                                                                                                    
                                                                                      the content of cognition; the main thing you are thinking about
thousand        denoting a quantity consisting of 1,000 items or units                                                                                             
                                                                                      the cardinal number that is the product of 10 and 100
throat          the part of an animal's body that corresponds to a person's throat                                                                                 
                                                                                      the passage to the stomach and lungs; in the front part of the neck below the chin and above the collarbone
throw           bedclothes consisting of a lightweight cloth covering (an afghan or bedspread) that is casually thrown over something                              
                                                                                      propel through the air
tick            make a sound like a clock or a timer                                                                                                               
                                                                                      sew
tiger           large feline of forests in most of Asia having a tawny coat with black stripes; endangered                                                         
                                                                                      a terrorist organization in Sri Lanka that began in 1970 as a student protest over the limited university access for Tamil students; currently seeks to establish an independent Tamil state called Eelam; relies on guerilla strategy including terrorist tactics that target key government and military personnel
time            adjust so that a force is applied and an action occurs at the desired time                                                                         
                                                                                      an instance or single occasion for some event
tin             plate with tin                                                                                                                                     
                                                                                      prepare (a metal) for soldering or brazing by applying a thin layer of solder to the surface
tire            exhaust or get tired through overuse or great strain or stress                                                                                     
                                                                                      hoop that covers a wheel
tissue          create a piece of cloth by interlacing strands of fabric, such as wool or cotton                                                                   
                                                                                      part of an organism consisting of an aggregate of cells having a similar structure and function
toaster         a kitchen appliance (usually electric) for toasting bread                                                                                          
                                                                                      someone who proposes a toast; someone who drinks to the health of success of someone or some venture
today           on this day as distinct from yesterday or tomorrow                                                                                                 
                                                                                      the day that includes the present moment (as opposed to yesterday or tomorrow)
toe             touch with the toe                                                                                                                                 
                                                                                      walk so that the toes assume an indicated position or direction
toilet          a plumbing fixture for defecation and urination                                                                                                    
                                                                                      a room or building equipped with one or more toilets
tomorrow        the next day, the day after, following the present day                                                                                             
                                                                                      the near future
tone            change the color or tone of                                                                                                                        
                                                                                      the quality of something (an act or a piece of writing) that reveals the attitudes and presuppositions of the author
tonight         during the night of the present day                                                                                                                
                                                                                      the present or immediately coming night
tool            ride in a car with no particular goal and just for the pleasure of it                                                                              
                                                                                      the means whereby some act is accomplished
top             reach or ascend the top of                                                                                                                         
                                                                                      finish up or conclude
tote            a capacious bag or basket                                                                                                                          
                                                                                      determine the sum of
touch           the event of something coming in contact with the body                                                                                             
                                                                                      the act of soliciting money (as a gift or loan)
tour            make a tour of a certain place                                                                                                                     
                                                                                      an industrial city in western France on the Loire River
tout            someone who buys tickets to an event in order to resell them at a profit                                                                           
                                                                                      advertize in strongly positive terms
towel           wipe with a towel                                                                                                                                  
                                                                                      a rectangular piece of absorbent cloth (or paper) for drying or wiping       
tower           a structure taller than its diameter; can stand alone or be attached to a larger building                                                          
                                                                                      a powerful small boat designed to pull or push larger ships
toy             an artifact designed to be played with                                                                                                             
                                                                                      any of several breeds of very small dogs kept purely as pets
trace           a drawing created by superimposing a semitransparent sheet of paper on the original image and copying on it the lines of the original image                                                                                              discover traces of
track           the act of participating in an athletic competition involving running on a track                                                                   
                                                                                      make tracks upon
trade           exchange or give (something) in exchange for                                                                                                       
                                                                                      the business given to a commercial establishment by its customers
trailer         a large transport conveyance designed to be pulled by a truck or tractor                                                                           
                                                                                      an advertisement consisting of short scenes from a motion picture that will appear in the near future
train           travel by rail or train                                                                                                                            
                                                                                      public transport provided by a line of railway cars coupled together and drawn by a locomotive
training        undergo training or instruction in preparation for a particular role, function, or profession                                                      
                                                                                      cause to grow in a certain way by tying and pruning it
treat           subject to a process or treatment, with the aim of readying for some purpose, improving, or remedying a condition                                  
                                                                                      provide treatment for
treatment       a manner of dealing with something artistically                                                                                                    
                                                                                      the management of someone or something
tree            chase an animal up a tree                                                                                                                          
                                                                                      plant with trees
trial           (law) the determination of a person's innocence or guilt by due process of law                                                                     
                                                                                      (sports) a preliminary competition to determine qualifications
trick           (card games) in a single round, the sequence of cards played by all the players; the high card is the winner                                       
                                                                                      an attempt to get you to do something foolish or imprudent
trip            make a trip for pleasure                                                                                                                           
                                                                                      put in motion or move to act
trump           play a trump                                                                                                                                       
                                                                                      a playing card in the suit that has been declared trumps
tub             the amount that a tub will hold                                                                                                                    
                                                                                      a relatively large open container that you fill with water and use to wash the body
tube            place or enclose in a tube                                                                                                                         
                                                                                      an electric railway operating below the surface of the ground (usually in a city)
tune            adjust the pitches of (musical instruments)                                                                                                        
                                                                                      the adjustment of a radio receiver or other circuit to a required frequency  
turn            cause to change or turn into something different;assume new characteristics                                                                        
                                                                                      cause to move around a center so as to show another side of
tutor           be a tutor to someone; give individual instruction                                                                                                 
                                                                                      act as a guardian to someone
twenty          the cardinal number that is the sum of nineteen and one                                                                                            
                                                                                      a United States bill worth 20 dollars
twin            either of two offspring born at the same time from the same pregnancy                                                                              
                                                                                      give birth to twins
twit            harass with persistent criticism or carping                                                                                                        
                                                                                      aggravation by deriding or mocking or criticizing
tyler           a town in northeast Texas                                                                                                                          
                                                                                      elected vice president and became the 10th President of the United States when Harrison died (1790-1862)
type            all of the tokens of the same symbol                                                                                                               
                                                                                      write by means of a keyboard with types
u               (chiefly British) of or appropriate to the upper classes especially in language use                                                                
                                                                                      a base containing nitrogen that is found in RNA (but not in DNA) and derived from pyrimidine; pairs with adenine
uniform         always the same; showing a single form or character in all occurrences                                                                             
                                                                                      provide with uniforms
university      a large and diverse institution of higher learning created to educate for life and for a profession and to grant degrees                           
                                                                                      the body of faculty and students at a university
upgrade         the act of improving something (especially machinery) by raising it to a higher grade (as by adding or replacing components)                       
                                                                                      give better travel conditions to
us              habitually do something (use only in the past tense)                                                                                               
                                                                                      North American republic containing 50 states - 48 conterminous states in North America plus Alaska in northwest North America and the Hawaiian Islands in the Pacific Ocean; achieved independence in 1776
va              the United States federal department responsible for the interests of military veterans; created in 1989                                           
                                                                                      a state in the eastern United States; one of the original 13 colonies; one of the Confederate States in the American Civil War
vacation        spend or take a vacation                                                                                                                           
                                                                                      leisure time away from work devoted to rest or pleasure
vacuum          the absence of matter                                                                                                                              
                                                                                      an empty area or space
van             any creative group active in the innovation and application of new concepts and techniques in a given field (especially in the arts)               
                                                                                      a truck with an enclosed cargo space
vi              the cardinal number that is the sum of five and one                                                                                                
                                                                                      more than 130 southeastern Virgin Islands; a dependent territory of the United States
video           (computer science) the appearance of text and graphics on a video display                                                                          
                                                                                      a recording of both the visual and audible components (especially one containing a recording of a movie or television program)
view            purpose; the phrase `with a view to' means `with the intention of' or `for the purpose of'                                                         
                                                                                      a personal belief or judgment that is not founded on proof or certainty      
virtue          a particular moral excellence                                                                                                                      
                                                                                      the quality of doing what is right and avoiding what is wrong
visit           come to see in an official or professional capacity                                                                                                
                                                                                      assail
voice           (linguistics) the grammatical relation (active or passive) of the grammatical subject of a verb to the action that the verb denotes                
                                                                                      utter with vibrating vocal chords
volume          a publication that is one of a set of several similar publications                                                                                 
                                                                                      the magnitude of sound (usually in a specified direction)
voucher         someone who vouches for another or for the correctness of a statement                                                                              
                                                                                      a document that serves as evidence of some expenditure
wait            wait before acting                                                                                                                                 
                                                                                      the act of waiting (remaining inactive in one place while expecting something)
wake            stop sleeping                                                                                                                                      
                                                                                      a vigil held over a corpse the night before burial
wale            thick plank forming a ridge along the side of a wooden ship                                                                                        
                                                                                      one of the four countries that make up the United Kingdom of Great Britain and Northern Ireland; during Roman times the region was known as Cambria
walk            a slow gait of a horse in which two feet are always on the ground                                                                                  
                                                                                      careers in general
wall            anything that suggests a wall in structure or function or effect                                                                                   
                                                                                      a layer of material that encloses space
want            hunt or look for; want for a particular reason                                                                                                     
                                                                                      be without, lack; be deficient in
warning         notification of something, usually in advance                                                                                                      
                                                                                      cautionary advice about something imminent (especially imminent danger or other unpleasantness)
warren          United States writer and poet (1905-1989)                                                                                                          
                                                                                      a colony of rabbits
wash            the erosive process of washing away soil or gravel by water (as from a roadway)                                                                    
                                                                                      a watercolor made by applying a series of monochrome washes one over the other
water           the part of the earth's surface covered with water (such as a river or lake or ocean)                                                              
                                                                                      once thought to be one of four elements composing the universe (Empedocles)  
wave            a hairdo that creates undulations in the hair                                                                                                      
                                                                                      a member of the women's reserve of the United States Navy; originally organized during World War II but now no longer a separate branch
wear            have in one's aspect; wear an expression of one's attitude or personality                                                                          
                                                                                      the act of having on your person as a covering or adornment
wed             having been taken in marriage                                                                                                                      
                                                                                      the fourth day of the week; the third working day
weed            any plant that crowds out cultivated plants                                                                                                        
                                                                                      clear of weeds
welcome         bid welcome to; greet upon arrival                                                                                                                 
                                                                                      the state of being welcome
western         relating to or characteristic of the western parts of the world or the West as opposed to the eastern or oriental parts                            
                                                                                      a film about life in the western United States during the period of exploration and development
wheel           game equipment consisting of a wheel with slots that is used for gambling; the wheel rotates horizontally and players bet on which slot the roulette ball will stop in                                                                   move along on or as if on wheels or a wheeled vehicle
whisper         speak softly; in a low voice                                                                                                                       
                                                                                      a light noise, like the noise of silk clothing or leaves blowing in the wind 
white           (usually in the plural) trousers made of flannel or gabardine or tweed or white cloth                                                              
                                                                                      a tributary of the Mississippi River that flows southeastward through northern Arkansas and southern Missouri
whore           have unlawful sex with a whore                                                                                                                     
                                                                                      compromise oneself for money or other gains
widget          a device or control that is very useful for a particular job                                                                                       
                                                                                      something unspecified whose name is either forgotten or not known
wife            a married woman; a man's partner in marriage                                                                                                       
                                                                                      provide with a wife; marry (someone) to a wife
will            leave or give by will after one's death                                                                                                            
                                                                                      a legal document declaring a person's wishes regarding the disposal of their property when they die
williams        English clergyman and colonist who was expelled from Massachusetts for criticizing Puritanism; he founded Providence in 1636 and obtained a royal charter for Rhode Island in 1663 (1603-1683)                                           United States playwright (1911-1983)
win             be the winner in a contest or competition; be victorious                                                                                           
                                                                                      something won (especially money)
wind            catch the scent of; get wind of                                                                                                                    
                                                                                      a musical instrument in which the sound is produced by an enclosed column of air that is moved by the breath
window          (computer science) a rectangular part of a computer screen that contains a display different from the rest of the screen                           
                                                                                      (trademark) an operating system with a graphical user interface
wing            the wing of a fowl                                                                                                                                 
                                                                                      stylized bird wings worn as an insignia by qualified pilots or air crew members
winner          the contestant who wins the contest                                                                                                                
                                                                                      a gambler who wins a bet
wire            string on a wire                                                                                                                                   
                                                                                      the finishing line on a racetrack
wish            prefer or wish to do something                                                                                                                     
                                                                                      invoke upon
wizard          possessing or using or characteristic of or appropriate to supernatural powers; ; ; ; - Shakespeare                                                
                                                                                      one who practices magic or sorcery
woman           a female person who plays a significant role (wife or mistress or girlfriend) in the life of a particular man                                      
                                                                                      women as a class
wood            a golf club with a long shaft used to hit long shots; originally made with a wooden head                                                           
                                                                                      the trees and other plants in a large densely wooded area
word            the divine word of God; the second person in the Trinity (incarnate in Jesus)                                                                      
                                                                                      the words that are spoken
work            cause to work                                                                                                                                      
                                                                                      (physics) a manifestation of energy; the transfer of energy from one physical system to another expressed as the product of a force and the distance through which it moves a body in the direction of that force
workday         a day on which work is done                                                                                                                        
                                                                                      the amount of time that a worker must work for an agreed daily wage
world           all of your experiences that determine how things appear to you                                                                                    
                                                                                      the concerns of this life as distinguished from heaven and the afterlife     
worry           touch or rub constantly                                                                                                                            
                                                                                      be concerned with
worshipper      a person who has religious faith                                                                                                                   
                                                                                      someone who admires too much to recognize faults
wound           an injury to living tissue (especially an injury involving a cut or break in the skin)                                                             
                                                                                      the act of inflicting a wound
writing         the activity of putting something in written form                                                                                                  
                                                                                      letters or symbols that are written or imprinted on a surface to represent the sounds or words of a language
yard            a long horizontal spar tapered at the end and used to support and spread a square sail or lateen                                                   
                                                                                      an enclosure for animals (as chicken or livestock)
yesterday       in the recent past; only a short time ago                                                                                                          
                                                                                      the recent past
zero            adjust (as by firing under test conditions) the zero of (a gun)                                                                                    
                                                                                      the sight setting that will cause a projectile to hit the center of the target with no wind blowing
zombie          several kinds of rum with fruit juice and usually apricot liqueur                                                                                  
                                                                                      a god of voodoo cults of African origin worshipped especially in West Indies
