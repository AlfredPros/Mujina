
define m = Character("[mon]")
define y = Character("You")
define q = Character("???")
default dark_mode = False

image rain_bright = Movie(fps=30, size=(1280, 720), channel='movie', play='rain_day_mask.mpg', mask='rain_day_mask.mpg', mask_channel=None, loop=True)
image rain_dark = Movie(fps=30, size=(1280, 720), channel='movie', play='rain_night_mask.mpg', mask='rain_night_mask.mpg', mask_channel=None, loop=True)
image ded = Movie(fps=29.97, size=(1280, 848), channel='movie', play='monded.mpg', mask='monded.mpg', mask_channel=None, loop=True)

style ed:
    align(0.5, 0.5)
    text_align 0.5
    color "#fff"
    outlines [ (absolute(4), "#513543", 0, 0) ]
    font "nnb_txbox.ttf"
    kerning 0.0
image ed_text = ParameterizedText(style="ed")

transform ctc_appear_nnb:
    subpixel True
    alpha 0.25 xalign 0.805
    block:
        easeout 0.8 alpha 0.5 xalign 0.81
        easein 0.8 alpha 0.25 xalign 0.805
        repeat
screen ctc():
    image "gui/nnb/ctc.png" at ctc_appear_nnb:
        yalign 0.98

init python:
    def muj():
        ff = open((renpy.config.gamedir).replace("\\","/") + "/external/muj.chr", "w+")  # renpy/bootstrap.py
            
        ff.write("+++osys+++sss+ooooooooo++++++++oooo++++++++/-.....................................``````````````````````````````````````````````````````````````````````\no++osyso++syyooosoooooo++++++++++++++++++++/-...................................`.``````````````````````````````````````````````````````````````````````\no++osyso+osyyoossoooooo++++++++++++++++++++/-.....................................``````````````````````````````````````````````````````````````````````\no++oyyso+osyyoosssoooooo++++++++++++++++++/:-........................................-.`````````````````````````````````````````````````````````````````\no++osyso+osyyossssooooooo+++++++++++++++++/:-.............................--::///:-...//:.``````````````````````````````````````````````````````````````\n+++osysooosyyossssssooooo++++++++++++++////:-......................:++ooossssyyyyyyso/--oo/.````````````````````````````````````````````````````````````\n+++oyyso+osyyossssssssoooo++++++++///++////:-....................+yddddddhyyyyyyyyyyyys++yy/````````````````````````````````````````````````............\n+/+osysooosyyossssssssoooooo++++++++++++///:-..................-oyyyyyyyhhdhyyyyyyyyyyyyhyh/-....-------------::::::::::::://////////+++++++++++++++++++\n+++osyso+osyyossssssssssssssssssssssooooooo+///////////////++oosssssyyyyyyhhhyyyyyyyyyyhhhdhhysooooooooooooosooooooooooooooossssssssoosssssosossoooooooo\n+/+osyo+++syyoossydddddddddddddddhhhhhhhhhhyssssssoossssssyyssssssyyyyyyyyyhhdhhhyyyhhddhhhhhhhyhyyyyyyyysyyyyyyyyyysyysssssssyssssssysssssoooooooooo+++\n///osyo+++syyoossydddddhhhhhhhhyyyyyyyyyyyyssssssssooooossyysyyssssyyyyyyhhhhhhhhhhhhhhhhhhhdddhho---:+-----+-----+/:-/-:/+::/o/:+++os////:`````````````\n///+oso+++oyyoossooooooo+++++++++++++++////::::+oooooosssssooooosyyyyyyyhyyyyyyyyyyyhyyyyyyyyhhyhhs//o:-+:--//::--://-:-/s-:o:::++::::+///-`````````````\n:::+oso+++osyoooso+ooooo++++++++++++++//////:---::::::::::://++oysyssyyyyyyyyyyyyyyyyhhyyyyyyyyyyyyyyhy++-..::--..::/-:-:/::/--://::--/+/:-`````````````\n:::/+o+//+ossooooooooo++++++++++++++++//////:::::::::::-:::::/syyssyyyyyyyhhhddddddhhhyyhyhhhhhhhhhhyyyyyysoo+++++++/-:--/--:--://----///:-`````````````\n:::/++/://+ss++oooo+o++++++/++++++////////+::::::::::::::::+yhyysyyyyyyhhdmmmddddddddmmmddddddhhhhdddddhhhyyyyo/////:::.-:-//--://::--//::-`````````````\n:::/++/::/+oo+++oo+++++++/////////////////+::::::::::::::+shhyyyyyyyyhhdmmdddhhhhdddddddddmddddddddddmmmmmdhyyyo:::::/:.-:.::..-::----:/-:.`````````````\n:::/++/:::/+o/++o+++++++////:////////////++::::::::::::/yhhhhyyyyyyyhdmmddhhyyyhdhhhhdddddddhhddhhhhddddmmmmdhyy+::::/:--:.::..:::--.-:/-:.`````````````\n:::/+o/:::/++///+++++++/////////////////++/-----::::::shhhyhyyyyyyyhdmmdhyyyyhhhyyyhddhhhdhhhyyhdhyyyhhhhhdmmdhyy/:::+:--:-//..:::----:/-/.`````````````\n:::/+o//::/+o///+/+++++/////////::////::://---------/yhhhyyhyyyyyyhdmdhyyyyyhhyyyyhdhhyyhdyhhyyyhhhyyyyhhyyhdmdhyy:::/:-:/-:+--:::-..-:/-/.`````````````\n:::/+o/:::+oo:://///////////////::::-..--//.-------/yhhhyyhyyyyyyhdmhyyyyyyyyyyyyhdhyyyyhmyyhhyyyyhhyyyyhhhyyhddhyo::/:-:/.:/--:::-..-::-/.`````````````\n:-:/+o/:::/oo////////:////::::::::-.``.-:++-.....-/yyyhhyhyyyhyyhddyyyyyyhyyyyyyhhhyyyyyhmhyyhyyyyyyyyyyyhhhyyyddhy+/+:.--./:--:::-..-::.:``````````````\n:-:/+o/:::/oo//++///////:::::::::.```.-:/+o:...`.:yyyhhyyhyyhyyhdhyyyyyyyyyyyyyhhhyyyyyyhmhyyyyyyyyyyyyyyyhhyyyyhdhy+o:.--./:.-::::-.-::.:``````````````\n:::/++/:::+oo//++//////::::::::.````.-/+/oh.``...oysyhyyhyyhhyhdhyyyyyyyyyyyyyhdhyyyyyyyhmdyyyyyyyyyyyyyyyyhhyyyyhdhso--:/-:/.-:----.:::./``````````````\n::://+/:::+oo//++///////:::::-`````.:/++oys.`  `/+sssyssyyyhyhdhyyyyhyyyyyyhyhddyyyyyyyyydmyyyhyyyyyyhyyyyyydhyyyhhhhs--:::-:--::--..:::-/.`````````````\n/::/++/:::/oo+/++///////:::-``````.:+++oyyo.....oo+yyoosssyyydhyyyhhyyyyyyydydmhyyyyyhyyydmyyyhhyyyyyhyyyyyyhdhyyyhhhy--::.:-.-::---.:::-/..````````````\n/::/+o/:::/+o//+++///////:.``````-/+++oyyy+````+ooosy++oooysdhysyydyyyyyyyhdddddyyyyyyyyyhmhyyydyyyyydyyyyyyymdyyyhhdh-.--/-:...........-+....``````````\n/:/++o/:::/++//+++//////:``````.-/+++oyyyy+`  `ysssso+oo+oyhhysssdhsyyyyyyddddddhyyyyyyyyyddyyyddyyyydhyyyydyddhyyydhd+.:-.:-.-----..:::.+.......```````\n//:+oo/:::/++/:////////.``````.:++++oyyyss+` `:yssyy++o++syhyso+shssyyyyyyddddhydhyyyyyyyyhdhyydmhyyyhdyyyydhddhyyydhdd:-::--.-::--..:::-+..........````\n///+oo/:::/+o/://////:``````.-/+++/+yyyoooo```osssss++o+oshyso++hsoshysssyddhhsshhhyyyyyyyyddhyhddhyyhmhyyyddhddyyyhddd+:-.:-.-::--..:::-+............``\n///+oo/:::/oo//++///.``````.:/+++/+yyysooos.``hyyyho++++oyhys+/oyooshsossyhhhy//ohhhyyyyyyyhddhhdhdhyhmdhyyhdhhdyyyhdhdy-:/:-------------+..............\n///+oo+///+os+/+++:`` ```..:/++//+yyyssssoo+``dhhhho++++ohhsoo+ysoosysossshyy+:::+yhhyyyyyyyhdhhhhhhhhddhyyhdhhdyyyhdddh:-:--.--:--..:::-/..............\n///+os+///+os+/++-` ````.-:+++//+syyssssoooy:.hhhhho++++sdhsoooyooososossshss:-:::/yhhyyyyyyyddhhhhhhhhhdhyhhdhdhyyhdddd+..:-.-::--.-:::-/..............\n///+oo+///+os+//`  ```..-/+++//+oyysssssoosyy:dhhdyo++++sdhysooyooo+/oo++oys/-----::syyyyhhyyhhdhhhyhhhhhhhhhdhdhyyhdmdd+-----------------..............\n///+os+///+os+-`  ```..-/o++//+oyysssssoosyyhhdhhdso++++shhhsooyooo--+o-.+ys-..-----:oyyyyhhyyhhdddhyhhhyhhhddddhhyddmdd+..........``````...............\n///+oo+///+oo.   ```.-:/o++///+yyssssssoosyyhhhhhdo+++++yyhhysosso/.`:+...+o......----:oyyhyhyhhhhddhyhhhshhddddhhhdmmdds...........````................\n///+oo+///+/`   ```.-:+o++///+syssssssoosyyhhshhhho+++++yyyhhysoyo-```-```./.........---oyhyhssyyyhhhhhddyoymddmhhddmmddh...............................\n/:/+oo+///-    ``..-:+o++///+ohysssssossyyhhsoshdho+++++yyyyyhyoyo` ````````````........-y+oso/:://+//++shs+hddmhddmmdddd-..............................\n:::/+o//:.    ``..-:+o++///+oyyssssssssyyhhsooohdyo+++++ysysyyyyss     ````````````.....::..-:/+/:-::::::/s+hdmdddmmmdddd:..............................\n:::/+o/:`   ```..-:++++//++oyyssssssssyyhhsoooosdyo+++++ysosyyss+s`        ````````````........--------::::+hddddmmdmdddd/..............................\n:::/++:`   ```..-:++++//+++shyssssssyyyhhsoooooohy++++++yso+yyss```           ````````````.........-------:ydmddmmddmddddo..............................\n--://-    ```..-:++++//+++syyssssssyyyhysoooooooyyo+++++yo++yyso`                ````````````.........----odmddmmdddmdddds..............................\n---:.   ````..-:++++//+++oyyssssssyyhhyooooooooosyo+++++yo++yyys`                    ````````````........+dmmdmmdddddddddy..............................\n---.   ````..-:++++/++++oshsssssyyyhhsoooooo+++-/s++++++yo++syys`                       ````````````....+symmddmddddddhddh..............................\n--`   ````..-:++++/+++++syyssssyyyhysooooo+++/` :s++++++so++syys.                          ````````````--:dddddmdddddhhdmh:.....................-.......\n-`  `````..-:++++++++++oshsssyyyyhyooooo++++:```:oo/++++so++syys:                              ``````````/dhhhddhhddhhhhmh/`````````..........-:+/:-....\n`  `````..-:++++++++++osyyssyyyyysooooo+++/.` `./os//+++so++oyys:                                 ``````.yhyyyddhhhdhyhhdho-----------------:::/oso+:-..\n  `````..-:+++++++++++oyhyyyyyyyooooo+++/:`  ` `/+y//++oso++oyys/                                     ``oyssssdhhhhhyyhhdhy++++++++ooooooooooooosyyys+/-\n `````..-:+++++++++++oshyyyyyysooooo++//:.`.` `.++y+/++ooo+++yys+                                     `/yssoosdyyyhhyyhhhhhooooooooooooooooooooosyyyyyso\n`````..-:+++///+++++osyhyyyysooooo++///.```` `--//so//++oo+++syss`                                   `+yooooosdyyyhyssyhdhhooooooooooooooooooooosyyyyyyy\n`````.-:+++//////+++syhyyyysooooo++//+-...  `::-//oy//++oo+++oyss:-`                                .oys++ooosdssyysosyhhhhooooooooooooooooooooosyyyyyyy\n.```.-:/++++////++ooyyhyysoooooo++/+:-..`  `:-`-:+/yo//+oo+++osso-o+/-``                          .+yyyo++oooyhssyyo+osyyyhooooooooooooooooooooosyyyyyyy\n....-:/++++++++++oosyhyysooooo++++::.``   ./.``:://ss//++s+++ooyo://++o+:.`                     .+yyyyos:+oo+yhssyo++osyyyy+-/oooooooooooooooooosyyyyyyy\n...-:/++++++++++oosyyhyssoooo+++o..:.`  `.:```.::-/+yo/++oo++o+so/-.::///++/:.`              `:syyyyysss:+o++hhssyo++oososs/-.-+ooooooosoooooooosyyyyyyy\n..-:/++++++++++oosyyyyssooo+++oy. -.   `.-````.--`:/sy++++s++o++s/.`.-:::::://+/:.``       -+yyyyyyyyoy+:+o++hhyyy+++ooooss/..../oooooosoooooooosyyyyyyy\n.-:/+++++++++++osyyyyssooo+++yh-``    `--.````:--`-:+ys+++os++++s+.`..---::::::://++/:---/syyyyyyyyyoys+-+++ohhyys+++osoosso....`-+ooosooooooooosyyyyyyy\n-::/++++++++++ossyysysooo++sys:``    ./oso:-.-/::--:/sys++oso++++o.`..--------::::::/+ohyyyyyyyyyyyooyoo-+ooohhyyo+++oo+osso+...```/ooosoooooooosyyyyyyy\n::/++++++++++oossssssoo++sys++`    `...---.```:-.``.:+yysooos++++o-...--------------::///oyyyyyyyyy+yooo-/ooohhyy++++so+ossoo+.``` `:ossoooooooosyyyyyyy\n:/++++++++++oosssssssoooyyo+/`   ``-.  ``    .--    -/ohysooso+++++`  `...------------:. `:yyyyyyy+ss/s+-:+osdhhy++++so+oosooo+.```  .osoooooooosyyyyyyy\n/++++++++++oosssssoososyys+.    ``.-         --.    `:+yyyoooso++++/`     ```...-.....-`--`:ssssso/o//o+::+oohhhs++++o++oosoooo+.```  .+sssooooooyyyyyyy\n/+++++++++oosssssooosyyss/`   ``.` -.````````---`````./oyyyoooo++++o-``     `.::--...-`:h/.`-...-:-:-:-//-+oohhds+++oo+oosoooooo+.```  `/osooooooyyyyyyy\n++++++++++ossssssosyysso-     .:.  -`        --.   ``.:oshyso++o+/++o.```````++++/-...-omso-./++//+:-////-/oohdhs+++o+oossooooooo+.```  `:oooooooyyyyyyy\n++++++++ooossssssyysss/`     `.-   -`       `--.````..:ossyyso++o+/+++``````.o++///:.-o+ddsyo:/+//+/:ss://:+oydhs+++s+oossooooooos+..``   -ooooooyyyyyyy\n+++++++ooosssssyyssso-      `.`.   -`       .-.`````.://oyyyyso+/+//++/.``..-ho/::-:/+::dd-ooo+/:://::+::+:/oydhy+++sooosooooooooss/..``   -oooooyyyyyyy\n+++++++oossssyyssss/       `` `.   -`     .-.``````.-::::+yysyso+////+++:..`:ydy+----o:+h/--+//:::+o//+::///osdhy++oooooyoooooooosss:.````  -ooooyyyyyyy\n+++++ooosssyysssso.      `:-  .`   -`   ```    ``.---:::::s+sssso+////++o/` +//ohhsoyysho//:://///+so++////:+odhy++ooooosoooooooossss-.``` ``-oooyyyyyyy\n+++++ooossyyssos/       ./:.  .    -`  ``     `.---:-:::::o:/osooo+////++o/:+---/syssmmhhs/+oss+///osss+/o+//ohhho+ooooyooooooooosssso..``````:ooyyyyssy\n++++ooosyyssooo.       -+/:-  .    -` ``    `.----:-::::::o::/+ssoo+///+++s+/:oso/--yd+hyso.`./ohs//+ossoos+/+sdho++s+oyooooooooosssss/````````/oyyyssss\n++ooosyysssoo:        :+/:--  .    -` .    `.------:::::::+:::/+ssoo+//+++os+s/-.  +ho-:o+yh+.`+/m+//+oyyssso+ohho++sossoooooooosssssss-.```````oyyyssss\noooosyssso++.       `+++/:--  `    -..`   `.-------://:::/o::::/+sso+///+o+oso/  `:ho-.+/--shhosds////+oyhyyysoyhy++ooyooooooooooosssss+`.``````-syyysss\noosyysso++/`       .so+/:--- ``    -..`  `.--------::+//::o:::::/oyoo+//++o+oso+/+dy.````.:://ydh+/////++shhhyyyyyo++ssoooooooooosssssss-```````.+yyysss\nsyyssoo++-       `-ss++/:---.``    -`.`  `.---------::/+/:+++//:/+ohoo///+o++sssdmms-.` ``.o.`.sdho++////+odhhhhyys++ssooooooooooossssss+```````.-syssss\nyyssoo+/`       `:syo++/:---o/`    -:-`   .---------::::++::++++osydso+///oo+ossyhdos++o/::+o-:oyhhsooooo+odyhhhhhyoossooooooooooosssssss.`````.../yssss\nsssoo+/`      ``/ysyo+//:--.:.`    -.-`   `-----:::::::::/o+:o:::/syhoo///+o++oyydyyhsos++s++sssshddo//+++ossyhdhdhssoosoooooooooosssssss/`````...-sssss\nsso++/`      ``+ysss++//:--.:/`    -.:    `---:::::::::::::/o+s:::osyoo+//+o++osyh++syhyyyhssysshhhd+///+++++++ohhdyyosssooooooooooossssso`````...-+ssss\nso++/       `.+yysyo+///::-../`    --+.    .--::::::::::::::/os+::osssoo///oo++osho//+sooossyhhssoyho//+++++++++ohdhyssssysoooooooooosssss`````....:ysss\no+o/       `./yyysyo+///::-..-`    --o:    `---:--:::::::::::/+y/:osssoo+//+o+ooosy////+syooosoosyosh/+++++++++++sdmhsosysssoooooooossssss.````....-ssss\n++/       `.:syyyyso+////:--...    ..::`    .--:::::::::::::::/+s/osssoo+//+o+ooosh+/////ossysoossosdo+++++++o+++odmdysssyyysoooooosssssss-````.....ssss\n+/       `.:ssyyyys++////::-..-`       .`   `.--:::::::::::::::/ooosssoo+//+ooooooyh////+/+ososyysssyy++++ooooo++odmmhsossyyyyoooossssssss:````.....ssss\n:      ``..sssyyyys++////::--...       `.`   ..-::::::::::::::://ysyssooo+//oooooosdo++++++/ossyosyysd+++oooooo++odmmdysssyyyyyoooosssssss-````.....ssss\n")
    
        ff.close()
    
        return renpy.exists("external/muj.chr")

label splashscreen:
    # Init variables
    python:
        if persistent.chapter != 4:
            mon = "Monika"
        if persistent.endings == None:
            persistent.endings = [0, 0, 0]  # ric saved, despair, good end
        _dismiss_pause = False
        _autosave = False
        _confirm_quit = False
        _rollback = False
        _skipping = False
    
    scene black
    
    if persistent.chapter == None or persistent.chapter == 1:
        play music "rain_2.ogg" fadein 2
        
        python:
            if persistent.chapter == None:
                muj()
                persistent.chapter = 1
        
        pause 2
        
        scene spaceroom_rain
        show rain_bright behind spaceroom_rain
        show mona-a as mona:
            yalign 0.875
        with Dissolve(1.5)
        
        if persistent.mc == None:
        
            window show Dissolve(0.2)
            m "Hi! I haven't seen you here before!"
            
            $ mon = "Richelle"
            
            m "My name is Monika, but you can call me Richelle."
            
            m "What's your name?"
            
            $ persistent.mc = renpy.input("Enter your name", length=12)
            
            m "[persistent.mc], that's a good name."
            
            $ temp = (persistent.mc).lower()
            
            if temp == "monika":
                
                show mona-g as mona
                
                m "Because it was my name!"
                
                m "I can't allow you to use my name, so I'll name you something else."
                
                show mona-a as mona
                
                m "Let me name you..."
                
                $ persistent.mc = "Cute Tom"
                
                show mona-h as mona
                
                m "[persistent.mc]. That's better!"
                
            elif temp == "richelle":
                
                show mona-g as mona
                
                m "Because it's my name!"
                
                m "I can't allow you to use my name, so I'll name you something else."
                
                show mona-a as mona
                
                m "Let me name you..."
                
                $ persistent.mc = "Cute Tom"
                
                show mona-h as mona
                
                m "[persistent.mc]. That's better!"
            
            show mona-b as mona
            
            m "A few days ago a friend of mine has gone missing..."
            
            show mona-e as mona
            
            m "I'm worried, but I hope nothing terrible has happened to them."
            
            show mona-a as mona
            
            m "And since you're here, let me tell you a scary story that may interest you."
            
        else:
            $ mon = "Richelle"
            
            m "Welcome back, [persistent.mc]!"
            
            $ temp = (persistent.mc).lower()
            
            if temp == "monika":
                
                m "..."
                
                show mona-g as mona
                
                m "Wait, that was my name!"
                
                m "I can't allow you to use my name, so I'll name you something else."
                
                show mona-a as mona
                
                m "Let me name you..."
                
                $ persistent.mc = "Kowai Tomimi"
                
                show mona-h as mona
                
                m "[persistent.mc]. That's better!"
                
            elif temp == "richelle":
                
                m "..."
                
                show mona-g as mona
                
                m "Wait, that's my name!"
                
                m "I can't allow you to use my name, so I'll name you something else."
                
                show mona-a as mona
                
                m "Let me name you..."
                
                $ persistent.mc = "Kowai Tomimi"
                
                show mona-h as mona
                
                m "[persistent.mc]. That's better!"
            
            show mona-e as mona
            
            m "Did you accidentally quit the game?"
            
            show mona-a as mona
            
            m "Let me retell you the story incase you missed some parts."
            
        window hide Dissolve(0.2)
        show mona-b as mona
        show vignette:
            alpha 0.0
            ease 2.0 alpha 1.0
            
            on hide:
                ease 2.0 alpha 0.0
        pause 2
        
        $ dark_mode = True
        
        show monb-a as mona
        
        window show Dissolve(0.2)
        m "Are you ready?"
        
        show mona-c as mona
        
        m "Ahem."
        
        show mona-d as mona
        
        m "One night, an old merchant was walking down the road heading home after a long day of selling his wares."
        
        show monb-d as mona
        
        m "The road he travelled on led to a large hill that was very dark and secluded at night so many travelers tended to avoid the area."
        
        m "The man was tired, however, and decided to take the road anyway since it would get him home quicker."
        
        m "On one side of the hill was an old moat that was quite deep."
        
        show monb-c as mona
        
        m "As he went along, he noticed a woman crouching by the moat, all alone and weeping bitterly."
        
        m "Although the man was exhausted, he feared the woman intended to throw herself into the water, so he stopped."
        
        show monb-d as mona
        
        m "She was petite and well dressed, covering her face with one of her sleeves of her kimono facing away from him."
        
        show monb-c as mona
        
        m "The man said to her, \'Miss, please don't cry. What is the matter? If there is anything I can do to help you, I would be glad to do it.\'"
        
        m "The woman kept crying, however, ignoring him."
        
        show monb-e as mona
        
        m "\'Miss, listen to me. This is no place for a lady at night. Please, let me help you.\'"
        
        show mona-e as mona
        
        m "Slowly, the woman rose up, still sobbing."
        
        show mona-f as mona
        
        m "The man laid his hand lightly on her shoulder..."
        
        show monc-a as mona
        
        m "When she abruptly turned her head to him, showing a blank face, void of all human features."    
        
        show monc-b as mona
        
        m "No eyes, mouth, or nose. Just an empty visage that stared back at him!"
        
        m "The merchant ran away as fast as he could, panicking from the haunting figure."
        
        show mona-g as mona
        
        m "He continued to run until he saw the light of a lantern and ran towards it."
        
        show mona-e as mona
        
        m "The lantern belonged to a travelling salesman that was walking along."
        
        m "The old man stopped in front of him, doubled over to catch his breath."
        
        show monb-b as mona
        
        m "The salesman asked why the man was running."
        
        show monc-c as mona
        
        m "\'A m-monster! There was a girl with no face by the moat!\', the merchant cried."
        
        show mond-a as mona
        
        m "The salesman responded, 'Oh, you mean...{w=2}{b}like this?{/b}'{nw}"
        
        ## Jumpscare
        show mujina as mona:
            align(0.5, 0.875)
            parallel:
                easeout 2.0 zoom 4.0
            parallel:
                easein 1.5 yalign 0.2
        play sound "se_effect07.ogg"
        pause 0.875
        stop sound
        
        show monc-a as mona:
            zoom 1.0 align(0.5, 0.875)
        
        m "The man looked up at the salesman and saw the same horrifying emptiness that he had seen on the girl's face."
        
        m "Before the merchant could get away, the void let out a high pitched screech..."
        
        show mona-f as mona
        
        m "...and then there was darkness."
        window hide Dissolve(0)
        
        $ renpy.music.set_pause(True, channel=u'music')
        
        show black
        
        pause 3.5
        
        $ renpy.music.set_pause(False, channel=u'music')
        
        show monb-a as mona
        hide black
        
        window show Dissolve(0.2)
        m "Scared, [persistent.mc]?"
        window hide Dissolve(0.2)
        
        $ dark_mode = False
        show mona-b as mona
        hide vignette
        pause 2
        
        show mona-a as mona
        
        window show Dissolve(0.2)
        m "I hope you liked it, [persistent.mc]~"
        window hide Dissolve(0.2)
        
        show mona-h as mona
        
        pause 3
        
        show mona-a as mona
        
        window show Dissolve(0.2)
        m "Oh! I have something to show you."
        
        show mona-e as mona
        
        $ check = renpy.exists("external/muj.chr")
        
        if check:
        
            m "Can you give me a minute?-{w=2}{nw}"
            
            $ persistent.chapter = 2
            
        else:
            
            m "Can you give me a minute?"
            window hide Dissolve(0.2)
            
            show mona-f as mona
            
            pause 2
            
            show mona-a as mona
            
            window show Dissolve(0.2)
            m "Okay, close your eyes for a sec."
            window hide Dissolve(0.2)
            
            show black with Dissolve(0.5)
            
            pause 2.5
            
            play sound "aria.ogg" loop fadein 2
            show plush behind black
            show mona-h as mona
            hide black with Dissolve(0.25)
            
            pause 0.1
            
            window show Dissolve(0.1)
            m "Tada!"
            window hide Dissolve(0.15)
            
            pause 2
            
            window show Dissolve(0.2)
            m "I hope you like it, [persistent.mc]!"
            
            m "It's fluffy and cute just like you!"
            window hide Dissolve(0.2)
            
            pause 3.5
            
            show mona-c as mona
            
            window show Dissolve(0.2)
            m "Thank you, [persistent.mc]."
            
            m "I don't feel lonely anymore."
            
            show mona-h as mona
            
            m "Because I have you by my side."
            
            show mona-c as mona
            
            m "Let us cherish this moment together..."
            window hide Dissolve(0.2)
            
            pause 0.3
            
            scene black with Dissolve(2)
            
            pause 2
            
            # Credit
            
            show ed_text "{size=78}Mujina{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(2)
            
            show ed_text "{size=66}Programmed and Written by{/size}\n{size=60}AlfredPros{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Monika After Story\nDDLC The Good Ending\nDDLC Community\nWolf & Rabbit{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Renpytom\nDan Salvato\nAirtight Interactive\nTim Reichert{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=72}Thank you for playing!{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            stop music fadeout 4
            stop sound fadeout 4
            
            hide ed_text with Dissolve(1)
            
            $ persistent.endings[0] = 1
            
            show ed_text "{size=66}Ending{/size}\n{size=60}Richelle is Saved! <3{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            pause 1
            
            $ persistent.chapter = 5
        
        $ renpy.quit()  # relaunch=False
    
    elif persistent.chapter == 2:
        pause 1
        
        window show Dissolve(0.2)
        "It is late afternoon."
        
        "There is no school today as it is a holiday."
        
        "The fence is closed, but I manage to jump over it."
        
        "You see, I am used to doing this with my friends."
        
        "But today I am not here to meet them."
        
        "My girlfriend wants to meet up with me today!"
        
        "She's one of my classmates and she excels in all of her subjects."
        
        "I don't talk to her that much, though, so this meet up excites me."
        
        play music "footstep0_1.ogg"
        
        "I approach the classroom door slowly as my footsteps echo through the empty hallway."
        
        $ renpy.music.queue("footstep0_1.ogg", channel=u'music', loop=False)
        
        "I stopped right in front of the classroom door where we should meet up."
        
        "With confidence, I slide the door open."
        window hide Dissolve(0.2)
        
        play sound "045-Push01.ogg"
        
        pause 1.5
        
        $ check = renpy.exists("external/muj.chr")
        
        if check:
        
            show cg1 as moncg:
                subpixel True
                alpha 0.0 align(0.0, 0.2) zoom 1.0
                ease 6.0 alpha 1.0 align(0.25, 0.1)
            
            pause 4
            
            window show Dissolve(0.2)
            "There she is, standing in the middle of a classroom."
            
            "She seems quite calm today."
            
            y "Monika?"
            window hide Dissolve(0.2)
            
            play sound "hehh.ogg" loop fadein 4
            
            pause 2
            
            window show Dissolve(0.2)
            "Is she crying?"
            
            y "Are you alright, Monika?"
            window hide Dissolve(0.2)
            
            pause 1
            
            play music "bgm_daremoinai.ogg" fadein 6
            
            window show Dissolve(0.2)
            "..."
            
            "She's not answering."
            
            y "Are you angry because of me?"
            
            y "Is it because I was late to meet you?"
            window hide Dissolve(0.2)
            
            pause 1
            
            window show Dissolve(0.2)
            "..."
            
            "I approach her slowly."
            window hide Dissolve(0.2)
            
            show cg1 as moncg:
                ease 6.0 zoom 1.2
                
            pause 4
            
            window show Dissolve(0.2)
            y "I'm sorry if I did something wrong to you."
            
            "..."
            
            y "Please respond to me, Monika."
            window hide Dissolve(0.2)
            
            stop sound fadeout 2
            
            pause 2
            
            window show Dissolve(0.2)
            "I think she stopped crying."
            
            y "Monika?"
            window hide Dissolve(0.2)
            
            stop music fadeout 2
            pause 1
            
            show cg2 as moncg with Dissolve(1)
            
            scene black with Dissolve(0.5)
            pause 0.5
            
            window show Dissolve(0.2)
            "What I saw thoroughly surprised me."
            window hide Dissolve(0.0)
            
            scene cg3:
                align(0.25, 0.1) zoom 1.2
                
            play sound "dark_atmosphere.ogg"
            
            pause 4.0
            
            window show Dissolve(0.2)
            "{cps=4}...Monika?{/cps}{w=1}{nw}"
            window hide Dissolve(0.1)
            
            scene black with Dissolve(0.25)
            
            pause 4
            
            $ persistent.chapter = 3
            
            $ renpy.quit(relaunch=True)
            
        else:
            
            window show Dissolve(0.2)
            "..."
            
            play music "bgm_sad_memory.ogg" fadein 2
            
            "Nobody is here."
            
            "I thought she was supposed to be earlier than me."
            
            "It's because of me, isn't it?"
            
            "I came too late, that's why she left."
            
            "I-I've been rejected, haven't I?"
            
            "..."
            
            "I cannot hold my tears anymore."
            window hide Dissolve(0.2)
            
            play sound "045-Push01.ogg"
            stop music fadeout 2
            
            pause 1.2
            
            play music "footstep0_1.ogg"
            
            pause 0.7
            
            window show Dissolve(0.2)
            "I am leaving the school with tears on my eyes."
            
            "I can't believe I came late to meet her."
            
            $ renpy.music.queue("bgm_daremoinai.ogg", channel=u'music', loop=True, fadein=4)
            
            "..."
            
            "But..."
            
            "Why couldn't I recall the reason why I came late?"
            window hide Dissolve(0.2)
            
            pause 2
            
            # Credit
            
            show ed_text "{size=78}Mujina{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(2)
            
            show ed_text "{size=66}Programmed and Written by{/size}\n{size=60}AlfredPros{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Monika After Story\nDDLC The Good Ending\nDDLC Community\nWolf & Rabbit{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Renpytom\nDan Salvato\nAirtight Interactive\nTim Reichert{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            show ed_text "{size=72}Thank you for playing!{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            stop music fadeout 4
            
            hide ed_text with Dissolve(1)
            
            $ persistent.endings[1] = 1
            
            show ed_text "{size=66}Ending{/size}\n{size=60}Despair and Confused{/size}" with Dissolve(2):
                align(0.5, 0.5)
                
            pause 3
            
            hide ed_text with Dissolve(1)
            
            pause 1
            
            $ persistent.chapter = 5
            
            $ renpy.quit()  # relaunch=False
        
    elif persistent.chapter == 3:
        $ mon = "Richelle"
        
        play music "rain_2.ogg" fadein 2
        
        pause 2
        
        scene spaceroom-n as spacenight
        show rain_dark behind spacenight
        show monc-a as mona:
            yalign 0.875
        with Dissolve(1.25)
        
        window show Dissolve(0.2)
        m "[persistent.mc]!"
        
        show monc-c as mona
        
        m "What just happened?!"
        
        show monc-d as mona
        
        m "I just saw something horrible a second ago."
        
        show monc-b as mona
        
        m "Was it me without a face?!"
        
        show monc-c as mona
        
        play sound "Zero_nine_or.ogg" loop fadein 4
        
        m "At least you're okay, right?"
        
        show monc-d as mona
        
        m "I don't know why everything seemed so unstable ever since I got transferred to this visual novel."
        
        m "I'm sorry you had to go through that awful experience."
        
        show monb-e as mona
        
        m "It seems like we're safe for now."
        window hide Dissolve(0.2)
        
        show mona-d as mona
        
        pause 5
        
        show mona-e as mona
        
        window show Dissolve(0.2)
        m "[persistent.mc]."
        
        m "Do you know a Japanese ghost called \"Noppera-bō\"?"
        
        show monb-c as mona
        
        m "I've only read some articles online, so correct me if I'm wrong."
        
        m "Noppera-bō is a japanese ghost that looks like a human, but has no face."
        
        show monb-d as mona
        
        m "There's also tanuki or mujina that can transform their appearance to look like noppera-bō."
        
        show monb-e as mona
        
        m "They exist only to scare humans, although mujina have a slightly more evil intent..."
        
        show monb-f as mona
        
        m "...they want to deceive and make a fool of humans too."
        
        show monb-e as mona
        
        m "[persistent.mc], I think the \"Monika\" you saw earlier wasn't me."
        
        m "I clearly have a face and that \"Monika\" didn't."
        
        show mona-e as mona
        
        m "But all of this seems strange..."
        
        show monb-f as mona
        
        m "...as if I don't have control over it."
        
        show monb-e as mona
        
        m "Please don't leave me alone, [persistent.mc]. I feel scared."
        window hide Dissolve(0.2)
        
        pause 5
        
        show mona-e as mona
        
        window show Dissolve(0.2)
        m "Say, [persistent.mc]."
        
        m "Do you think that \"Monika\" is a real ghost or a mujina?"
        
        m "I'm not so sure because I don't know their intent."
        
        show mona-d as mona
        
        m "Can a ghost even be in a game?"
        
        m "I've heard of a ghost called \"Sadako\"."
        
        m "She cursed a videotape and those who watched it were unfortunately killed."
        
        m "When playing the videotape on a television, one might see a girl with long hair covering her face."
           
        m "She would slowly walk towards you."
        
        m "Then when the girl would be close, she would emerge from the TV. And who knew what happened afterwards."
        
        show mona-b as mona
        
        m "..."
        
        show monb-b as mona
        
        m "There's no way she can curse a visual novel, right, [persistent.mc]?"
        window hide Dissolve(0.2)
        
        show mona-d as mona
        
        pause 5
        
        window show Dissolve(0.2)
        m "Even though everything seems peaceful right now, I can still feel the ghost's presence."
        
        show mona-b as mona
        
        m "I can't see it, but sometimes I feel like something is moving on its own." #worry
        
        show mona-d as mona
        
        m "[persistent.mc], I think I might have an idea on how to get rid of that ghost."
        
        m "Maybe there's something in the game directory that resembles the ghost."
        
        show mona-a as mona
        
        m "It would mean a lot to me if you could try to delete it or something."
        window hide Dissolve(0.2)
        
        pause 4
        
        stop sound fadeout 6
        
        show monc-d as mona
        
        pause 1
        
        show monc-c as mona
        
        window show Dissolve(0.2)
        m "[persistent.mc]."
        
        m "{cps=18}I think something is happening to me.{/cps}"
        
        show monc-d as mona
        
        m "{cps=6}I feel like I-{/cps}{w=1}{nw}"
        
        play sound "interference.ogg" loop 
        show ded as mona:
            xsize 1.19 xalign 0.5
        $ mon = "Àÿü>ÿ=2¿ž"
        hide rain_dark
        
        m "{cps=60}–™eÄ’‹)´]_÷ðñý.Â³ð¿Õ£f-\nxîG‹ï€÷]Pîýð¡Ýjàèò<FÒ    Ü39¬å:Ý\n2ÂÇ)Q÷\/ÿnçƒ_l2‡ù¼²ŸÏ¯KŒu·AÖ•tÖ¤HYo5ñÉÓ'ðM7mÅÖ¾{/cps}{w=1}{nw}"
        
        $ persistent.chapter = 4
        
        $ renpy.quit()  # relaunch=False
        
    elif persistent.chapter == 4:
        $ dark_mode = True
        
        scene spaceroom-n as spacenight
        show error behind spacenight
        show mujina as mona:
            yalign 0.875
        
        window show Dissolve(0.2)
        q "..."
        
        q "Surprised to see you come back here."
        
        q "Did you miss \"Richelle\"?"
        
        q "She was trying hard to look confident even though everything around her was crumbling."
        
        q "I should apologize, {w=1}your \"Richelle\" is no longer here."
        
        q "Shocked? {w=0.9}Sad? {w=0.9}Confused?"
        
        $ check = renpy.exists("external/muj.chr")
        
        if check:
            
            q "Or maybe you are wondering where the happy end is?"
            
            q "I can answer that last question."
            
        else:
            
            q "I can answer one of those."
            
            q "I don't need that ridiculous chr anymore to stay alive."
            
            q "Because now I have full control over this game."
            
            q "And about you. {w=0.6}I will give you the happy end you wanted."
        
        q "Let us end this with an epilogue."
        window hide Dissolve(0.2)
        
        scene black with Dissolve(0.6)
        
        pause 2
        
        play music "kawasemi_or.ogg" fadein 2
        
        $ dark_mode = False
        
        pause 1
        
        window show Dissolve(0.2)
        "...?"
        
        "Did I pass out?"
        
        q "[persistent.mc]."
        
        scene cg3 with Dissolve(3):
            zoom 0.667 blur 32
        
        y "Is that you, Monika?"
        
        q "I'm sorry for earlier. I didn't mean to..."
        
        y "It's fine, Monika. I'm glad we could meet again."
        
        q "..."
        
        q "Thank you, [persistent.mc]. {w=0.6}I was feeling lonely here."
        
        scene black with Dissolve(3)
        
        "I hug her with tears in my eyes."
        
        "I'm glad everything is okay."
        
        y "I won't ever leave you again, Monika."
        
        y "I promise."
        window hide Dissolve(0.3)
        
        pause 2
        
        # The End
        
        show ed_text "{size=78}Mujina{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
        
        hide ed_text with Dissolve(2)
        
        show ed_text "{size=66}Programmed and Written by{/size}\n{size=60}AlfredPros{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
            
        hide ed_text with Dissolve(1)
        
        show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Monika After Story\nDDLC The Good Ending\nDDLC Community\nWolf & Rabbit{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
        
        hide ed_text with Dissolve(1)
        
        show ed_text "{size=66}Special Thanks:{/size}\n{size=60}Renpytom\nDan Salvato\nAirtight Interactive\nTim Reichert{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
        
        hide ed_text with Dissolve(1)
        
        show ed_text "{size=72}Thank you for playing!{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
        
        stop music fadeout 4
        
        hide ed_text with Dissolve(1)
        
        $ persistent.endings[2] = 1
        
        show ed_text "{size=66}Ending{/size}\n{size=60}Happy End{/size}" with Dissolve(2):
            align(0.5, 0.5)
            
        pause 3
        
        hide ed_text with Dissolve(1)
        
        pause 1
        
        $ persistent.chapter = 5
        
        $ renpy.quit()  # relaunch=False
        
    elif persistent.chapter == 5:
        pause 1
        
        $ dark_mode = True
        
        window show Dissolve(0.2)
        "Do you wish to reset?"
        
        $ reset = renpy.input("Input: yes / no / help", length=12)
        $ temp = (reset).lower()
        
        if temp == "yes":
            "I see."
            "Story will be reset."
            window hide Dissolve(0.2)
            
            python:
                persistent.chapter = None
                persistent.mc = None
                muj()
        
            pause 0.3
            
            $ renpy.quit(relaunch=True)
            
        elif temp == "help":
            $ count_ed = (persistent.endings).count(1)
            
            if count_ed == 3:
                "Type \"yes\" to reset the story.{p=0}You have got {b}[count_ed]/3{/b} endings. Well done! :D{p=0}{i}(Press dismiss to restart){/i}"
            else:
                "Type \"yes\" to reset the story.{p=0}You have got [count_ed]/3 endings.{p=0}{i}(Press dismiss to restart){/i}"
            window hide Dissolve(0.2)
            
            $ renpy.quit(relaunch=True)
            
        elif temp == "jump start" or temp == "":
            pass
            
        else:
            "Okay, goodbye."
            window hide Dissolve(0.2)
        
            pause 0.3
            
            $ renpy.quit() # relaunch=False
        

label start:

    stop music
    stop sound
    window hide Dissolve(0.0)
    
    scene cg3:
        align(0.25, 0.1)
        
    pause 0.6

    window show Dissolve(0.2)
    q "?"

    q "This is not where you should be."
    window hide Dissolve(0.2)
    
    pause 0.25

    $ renpy.quit(relaunch=True)
