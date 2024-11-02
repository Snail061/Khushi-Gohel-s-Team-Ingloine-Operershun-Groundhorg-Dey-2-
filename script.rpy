# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define n = Character("Da Narrator")
define s = Character("Shelly")
define u = Character("Ur mom")
define y = Character("you")
define g = Character("Neil")
define p = Character("Generic family")
define t = Character("Tiffany")
define d = Character("da Door")
define a = Character("Seamus")
define b = Character("Generic kidnapped kid")
define r = Character("+=*=+*(((telaportashun)))*+=*=+")

# The game starts here.

label start:
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene kos

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
    voice"nar/nar1.MP3"
    n "De groundhog iz running frantically to the hole in the snow "
    voice"nar/nar2.MP3"
    n "Ground hog quickly goes into the burrow"
    scene kso
    voice"nar/nar3.MP3"
    n "as chubby as it is, it still fits, and goes into the hole"


    # start scene 3
    scene titll
    show ujuj
    voice"nar/nar4.MP3"
    n "at the entrance you are greeted by your coworker Shelly"
    voice"shelly/line1.MP3"
    s "Oi floofster , how’s the weather?"


    menu:
        "It's pretty cold":
            jump choice1_cold
        "Its nuts":
            jump choice1_nuts
        "Nice and warm":
            jump choice1_warm

    label choice1_cold:
        voice"shelly/linee2.MP3"
        s "Eh it’ll get betah"
        voice"shelly/line3.MP3"
        s "letz get back to work"
        menu:
            "OK Boomer":
                jump choice2_boomer
            "sure":
                jump choice2_sure
            "Shucky darns!!":
                jump choice2_sure

        label choice2_boomer:
            voice"nar/nar7.MP3"
            n "Shelly starts examining you"
            voice"nar/nar10.MP3"
            n "She mutters under breath “ok boomer” sneeringly"
            voice"nar/nar11.MP3"
            n "(Then a look of alertness )"
            voice"shelly/line4.MP3"
            s "Hmmm …"
            voice"shelly/line5.MP3"
            s "Have you been sniffing oregano?"
            voice"you/o1.MP3"
            y "no"
            voice"shelly/line4.MP3"
            s "Hmmm..."
            voice"shelly/lin7.MP3"
            s "turn your head"
            menu:
                "Turn your head to the right":
                    jump choice3_pellets
                "turn your head to the left":
                    jump choice3_rash

            label choice3_pellets:
                voice"shelly/line8.MP3"
                s "Holy Pellets! Thats a bad case of ticks"
                voice"shelly/line9.MP3"
                s "Go to the doctor"
                voice"you/o2.MP3"
                y "Right now?"
                voice"shelly/lin10.MP3"
                s "just kidding (lol)"
                voice"shelly/line11.MP3"
                s "we don't even have a doctor currently"
                jump choice3_done

            label choice3_rash:
                voice"shelly/line12.MP3"
                s "Rancid! That's a pretty nasty rash"
                voice"shelly/line9.MP3"
                s "Go to the doctor"
                voice"you/o2.MP3"
                y "Right now?"
                voice"shelly/lin10.MP3"
                s "just kidding (lol)"
                voice"shelly/line11.MP3"
                s "we don't even have a doctor currently"

                jump choice3_done
            label choice3_done:
            jump choice2_done

        label choice2_sure :
            voice"shelly/lin13.MP3"
            s "Ok get lets get ready"
            voice"shelly/lin14.MP3"
            s "Repeat after me “I AM A BIG FURRY GROUND HOG”"
            voice"you/o3.MP3"
            y "“I AM A BIG FURRY GROUND HOG”"
            voice"shelly/line15.MP3"
            s "“I CAN BRAVE THE COLD”"
            voice"you/o4.MP3"
            y "Heh?"
            voice"shelly/lin16.MP3"
            s "Winter’s over"
            voice"shelly/lin20.MP3"
            s "Its teh first day back and already lethargic "
            voice"nar/nar12.MP3"
            n "( says sarcastically)"
            voice"shelly/lett.MP3"
            s "You need to restock the lettuce"
            voice"shelly/lin22.MP3"
            s"Yer going back outside"
            jump choice2_done

        label choice2_done:
        jump choice1_done
    label choice1_nuts:
        voice"shelly/lin23.MP3"
        s "haha good one"
        voice"shelly/lin24.MP3"
        s "eh want some pecans?"
        menu:
            "Sure":
                jump choicee2_sur
            "Nah":
                jump choicee2_nah

        label choicee2_sur:
            voice"shelly/line25.MP3"
            s "Here ya go"
            voice"shelly/line26.MP3"
            s "us ground hogs have gotta celebrate Ground hog day!"
            voice"shelly/line28.MP3"
            s "don'tell my boss (lol)"
            voice"nar/clink.MP3"
            n "(Pecans clink)"
            jump choicee2_done

        label choicee2_nah:
            voice"shelly/jorjor.MP3"
            s "straight up jorsey! "
            voice"shelly/auii.MP3"
            s "you sure?"

            menu:
                "okay i'll take a few":
                    jump choice4_ok
                "Yea":
                    jump choice4_yea

            label choice4_ok:
                voice"shelly/line25.MP3"
                s "Here ya go"
                voice"shelly/line26.MP3"
                s "us ground hogs have gotta celebrate Ground hog day!"
                voice"shelly/line28.MP3"
                s "don'tell my boss lol"
                voice"nar/clink.MP3"
                n "(Pecans clink)"
                jump choice4_done

            label choice4_yea:
                voice"shelly/linebobo1.MP3"
                s "You will get too thin and then die"
                voice"shelly/linebobo2.MP3"
                s "You sureeeee  u dont want some?"
                menu:
                    "okay i'll take a few":
                        jump chu_ok
                    "nah, really I don’t want to ":
                        jump chu_no

                label chu_ok:
                    voice"shelly/line4.MP3"
                    s "Hmmm …"
                    voice"shelly/line25.MP3"
                    s "Here ya go"
                    voice"shelly/line26.MP3"
                    s "us ground hogs have gotta celebrate Ground hog day!"
                    voice"shelly/line28.MP3"
                    s "don'tell my boss lol"
                    voice"nar/clink.MP3"
                    n "(Pecans clink)"
                    jump chu_done

                label chu_no:
                    voice"shelly/poofgone.MP3"
                    s "That indigestion you were complaining about *poof* gone"
                    voice"shelly/softc.MP3"
                    s "You realy dont want some?"
                    menu:
                        "fine , give me some":
                            jump chun_ok
                        "I don’t have indigestion anymore":
                            jump chun_no

                    label chun_ok:
                        voice"shelly/jobo5.MP3"
                        s "Gudnooss grachus, here ya go"
                        voice"shelly/line26.MP3"
                        s "us ground hogs have gotta celebrate Ground hog day!"
                        voice"shelly/line28.MP3"
                        s "don'tell my boss lol"
                        voice"nar/clink.MP3"
                        n "(Pecans clink)"
                        jump chun_done

                    label chun_no:
                        voice"shelly/jubjob.MP3"
                        s "Doofus, Just take em’ already, spare the script writer"
                        menu:
                            "fine , give me some":
                                jump yuh_ok
                            "i'll pass":
                                jump yuh_no

                        label yuh_ok:
                            voice"shelly/qwerty.MP3"
                            s "Gudnooss grachus, ya go ya big stupid ground hog"
                            voice"shelly/line28.MP3"
                            s "don'tell my boss lol"
                            voice"nar/clink.MP3"
                            n "(Pecans clink)"
                            jump yuh_done

                        label yuh_no:
                            voice"shelly/corectomundo.MP3"
                            s "That was straight up joursey Eh? ya big stupid ground hog"
                            jump yuh_done
                        label yuh_done:
                        jump chun_done
                    label chun_done:
                    jump chu_done
                label chu_done:
                jump choice4_done
            label choice4_done:
        label choicee2_done:
        jump choice1_done

    label choice1_warm:
        voice"shelly/sewa1.MP3"
        s "Tats the ground hog spirt"
        voice"shelly/sewa2.MP3"
        s "you've been working hard today, you can leave early "
        voice"you/o4.MP3"
        y "Thanks"
        voice"shelly/sewa3.MP3"
        s "Don’t mention it"
        voice"shelly/sewa6.MP3"
        s "Oh by the way did you hear about the ticks going around?"

        menu:
            "Uhh .. maybe , .., yes":
                jump uu_ok
            "no":
                jump uu_no

        label uu_ok:
            voice"shelly/gobsam.MP3"
            s "Really!? Did Chungus or Chunker tell ye"
            menu:
                "Chunker":
                    jump fat1_oh
                "Chungus":
                    jump fat1_no
            label fat1_oh:
                voice"shelly/nerp.MP3"
                s "Aeh that blabber mouth "
                voice"you/o4.MP3"
                y "(sigh in relief due to not getting caught lying)"
                jump fat1_done
            label fat1_no:
                voice"shelly/nerp.MP3"
                s"Aeh that blabber mouth"
                voice"you/o4.MP3"
                y "(sigh in relief due to not getting caught lying)"
                jump fat1_done
            label fat1_done:
            jump uu_done

        label uu_no:
            voice"shelly/niiis.MP3"
            s "Well now you know :)"
            voice"shelly/chunkchunk.MP3"
            s "one of the chunker twins told me"
            voice"shelly/lllls.MP3"
            s "watch out for them..."
            jump uu_done
        label uu_done:
        jump choice1_done
    label choice1_done:
    voice"shelly/doe1.MP3"
    s "also, before you do anything"
    voice"shelly/doe2.MP3"
    s "give this package to neil"
    s "(hands you a package)"
    voice"shelly/doe55.MP3"
    s "He should be there by the end of the hallway"
    scene fun
    voice"nar/nar20.MP3"
    n "as you enter the hallway you noice weird sign"
    voice"nar/nar21.MP3"
    n "you wait for 10 clicks cuz this looks kinda interesting"
    voice"you/o7.MP3"
    y "1"
    voice"you/o8.MP3"
    y "2"
    voice"you/o9.MP3"
    y "3"
    voice"you/o10.MP3"
    y " nevermind this is a lot of clicking"
    voice"nar/nar22.MP3"
    n "you end up waiting for 3 clicks"
    voice"nar/nar26.MP3"
    n " as soon as you start to leave a very sad generic family appears"
    show generic
    voice"nar/nar27.MP3"
    n "from the photo they are carrying, along with that unedited background"
    voice"nar/nar28.MP3"
    n " you realize something bad has happened !!! :("
    voice"nar/nar30.MP3"
    n "after seeing their sad generic plight you decide to talk to them"
    voice"you/o19.MP3"
    y "i am so sorry for your loss"
    voice"you/ca1.MP3"
    p "thanks yous sobs thanks yous sobs"
    voice"you/o4.MP3"
    y " what happened?"
    voice"you/ca2.MP3"
    p " but sobs ... we lost him .. in the generic supermarket ..sobs"
    voice"you/ca3.MP3"
    p " sobbs.. Seamus ..sobss.. the mouse  kidnapped 'im ..sobs"
    menu:
        "help them find their kid":
            jump ji_ok
        "give them neils package":
            jump ji_no

    label ji_ok:
        voice"you/c4.MP3"
        p "really?"
        voice"you/c5.MP3"
        p "thanks yous sos muchs sobs"
        voice"you/c6.MP3"
        p "generally we loose sobs two each year"
        voice"you/c8.MP3"
        p " we guess this year it will only be 1  sobs!"
        jump ji_done

    label ji_no:
        voice"you/c9.MP3"
        p "(opens package)"
        voice"you/c10.MP3"
        p " Woah!..sobs Its a letter of secomandation for your promotion!"
        voice"you/c11.MP3"
        p "It says you are sobs, intelligent, sobs, resourfull, kind, awesome"
        voice"you/c18.MP3"
        p "ect, sobs, blah blah blah, sobs ,yadda yadda "
        voice"nar/mu1.MP3"
        u "Generic Family used Flattery it was Super effective!"
        voice"nar/chingoo.MP3"
        n " you get verry flattered and decide to help them"
        voice"you/ohmy.MP3"
        y " stop sobbing I will find your very generic child"
        voice"you/c20.MP3"
        p "yay"


        jump ji_done
    label ji_done:

    scene gus
    voice"nar/q1.MP3"
    n "you continue down the hallway in scearch of the generic child"
    voice"nar/q2.MP3"
    n "gosh danrabbit!!"
    voice"nar/q3.MP3"
    n " there are three generic tunnels"

    menu:
        "generic tunnel 1":
            jump j_1
        "hint hint wink wink generic tunnel 2":
            jump j_2
        "generic tunnel 3":
            jump j_3

    label j_1:
        voice"nar/q6.MP3"
        n " generic tunnel l one enters into generic tunnel two"
        voice"nar/q7.MP3"
        n " The hint was pretty obivios i think"
        voice"nar/q8.MP3"
        n "ya nitwit"
        voice"nar/t1.MP3"
        n " anyways scince it is very long"
        voice"nar/t2.MP3"
        n " i shall tell you the  preamble to the bee movie"
        voice"nar/t3.MP3"
        n " According to every nown leys of aviation"
        voice"nar/t4.MP3"
        n "an bee"
        voice"nar/t5.MP3"
        n " never mind, we reached tunnel 2"
        voice"nar/w1.MP3"
        n " the tunnel is pitch black"
        voice"nar/w2.MP3"
        n" you can smell the damp walls, wet from the incoming snow"
        voice"nar/w6.MP3"
        n " soon you emerge out the tunnel and onto the surface"
        jump j_done

    label j_2:
        voice"nar/g1.MP3"
        n "we enter hint hint wink wink generic tunnel 2"
        voice"nar/g2.MP3"
        n "I hope the hint helped "
        voice"nar/w1.MP3"
        n " the tunnel is pitch black"
        voice"nar/w2.MP3"
        n" you can smell the damp walls, wet from the incoming snow"
        voice"nar/w6.MP3"
        n " soon you emerge out the tunnel and onto the surface"

        jump j_done

    label j_3:
        voice"nar/g4.MP3"
        n " generic tunnel 3 one enters into generic tunnel two"
        voice"nar/q7.MP3"
        n " The hint was pretty obivios i think"
        voice"nar/q8.MP3"
        n "ya nitwit"
        voice"nar/t1.MP3"
        n " anyways scince it is very long"
        voice"nar/t2.MP3"
        n " i shall tell you the  preamble to the bee movie"
        voice"nar/t3.MP3"
        n " According to every nown leys of aviation"
        voice"nar/t4.MP3"
        n "an bee"
        voice"nar/t5.MP3"
        n " never mind, we reached tunnel 2"
        voice"nar/w1.MP3"
        n " the tunnel is pitch black"
        voice"nar/w2.MP3"
        n" you can smell the damp walls, wet from the incoming snow"
        voice"nar/w6.MP3"
        n " soon you emerge out the tunnel and onto the surface"
        jump j_done
    label j_done:
    scene tfr
    voice"nar/q11.MP3"
    n "you encounter a mysterious animal"
    voice"nar/q12.MP3"
    n "one that no groundhorg has ever layed eyes on before"
    voice"nar/q13.MP3"
    n " you bask in its glory, and then decide it is your supreme leader"
    voice"you/whomp.MP3"
    y "hello, almighty creature, what is your magnificencess name?"
    voice"shelly/tiff1.MP3"
    t "call me tiffany"
    voice"you/o2.MP3"
    y "uhh okey"
    voice"you/hu.MP3"
    y " your lordess tifffany , by any chance "
    voice"nar/q17.MP3"
    n " she cuts your sentence"
    voice"shelly/tiff2.MP3"
    t " sure, i'll do it if you have ants"
    voice"shelly/tiff3.MP3"
    t "i'm guessing you are looking for seamus the mouse"
    voice"shelly/iff6.MP3"
    t " so ya got ant?!?!?!"
    voice"you/shu.MP3"
    y "i can probably get them to your pious self, soon i think, probably"
    voice"shelly/ant.MP3"
    t "okay then hurry along and grab some ants"
    voice"nar/q21.MP3"
    n " leaving the mystical creature ,you head back"
    voice"nar/q22.MP3"
    n "through the tunnel and into the hallway"

    scene gus
    menu:
        "you continue looking for seamus":
            jump yy_a
        "You give her some ticks that are on your back instead of ants":
            jump yy_b
        "you actually look for ants":
            jump yy_c
    label yy_a:
        voice"nar/w20.MP3"
        n "you check around the tunnel"
        voice"nar/w24.MP3"
        n "no seamus"
        voice"nar/r1.MP3"
        n "you shout - SEAMUS !!!"
        voice"nar/nos.MP3"
        n "no seamus"
        voice"nar/r2.MP3"
        n "you scream - SeAmUs"
        voice"nar/nos.MP3"
        n "no seamus"
        voice"nar/r3.MP3"
        n " you yodel - SEAMUSUSUSUSUOLDEAOOO"
        voice"nar/nos.MP3"
        n "no seamus"
        voice"nar/y2.MP3"
        n "you echo seamus into the tunell"
        voice"nar/y3.MP3"
        n "- seamus    ... seamuss.....seamuussss"
        voice"nar/y4.MP3"
        n "still no seamus"
        voice"nar/y5.MP3"
        n " you realize that seamus can't hear you"
        voice"nar/y6.MP3"
        n  "so, you stop using your voicebox"
        voice"nar/y7.MP3"
        n " you start searching for seamus again"
        voice"nar/y8.MP3"
        n "soon , you smell cheese"
        jump yy_done
    label yy_b:
        voice"nar/y9.MP3"
        n "you slowly try to pry one off your back"
        voice"nar/y0.MP3"
        n "you see a generic tick"
        voice"nar/y11.MP3"
        n " you are very scared of generic ticks"
        voice"nar/y12.MP3"
        n " you pass out"
        voice"nar/y13.MP3"
        n " some generic ticks start plaing tick tack toe on top of your feet"
        voice"nar/y14.MP3"
        n " you wake up and forget about ticks"
        voice"nar/y15.MP3"
        n " you smell cheese"
        jump yy_done
    label yy_c:
        voice"nar/y16.MP3"
        n " you spot some vegetation that looks green"
        voice"nar/y17.MP3"
        n " then you realize its actually fungus"
        voice"nar/y18.MP3"
        n "what a fungi (lol)"
        voice "nar/y19.MP3"
        n " but you can't really tell"
        voice"nar/y20.MP3"
        n " partially because the artist hasn't gone outside in 10 years"
        voice"nar/y21.MP3"
        n "and partially because you smell some cheeze"

        jump yy_done
    label yy_done:
    voice"nar/y22.MP3"
    n "since cheese means mouse"
    voice"nar/y23.MP3"
    n" you decide to find where the smell is comming from"

    scene sji
    voice"nar/y24.MP3"
    n "I the narrator think this doesn't make sense"
    voice"nar/y25.MP3"
    n " this house was in apporximately 3 parallell universes away"
    voice"nar/y26.MP3"
    n " anyways due to plot convinieance and your apparent telaportation powers"
    voice"nar/y27.MP3"
    n "  you have found seamus's house"
    voice"nar/y28.MP3"
    n " see it even has a sign saying it is!"
    menu:
        "Break door open":
            jump que_1
        "Straight up leave":
            jump que_2
        "try a password on the key pad":
            jump que_3
    label que_1:
        voice"nar/y29.MP3"
        n " you use all of your strength"
        voice"nar/y30.MP3"
        n " the door doesnt budge"
        voice"nar/y31.MP3"
        n " in fact why don't you the reader help your charecter out"
        voice"nar/y32.MP3"
        n " you guess if you click fast the door will open"
        voice"nar/y33.MP3"
        n " because that makse sence very much sense"
        voice"nar/y34.MP3"
        n "you proceed to have to click very fast to open the door"
        voice"nar/y35.MP3"
        n " the space bar preferrablly"
        voice"nar/y36.MP3"
        n "no special reason but I just like using the space bar"
        voice"nar/p1.MP3"
        n "punch"
        voice"nar/p2.MP3"
        n "punch punch"
        voice"nar/p3.MP3"
        n "punch punch bang"
        voice"nar/p4.MP3"
        n "punch punch bang bam"
        voice"nar/p5.MP3"
        n "punch punch punch bang bam boom"
        voice"nar/p6.MP3"
        d "crash"
        voice"nar/p7.MP3"
        n "the door has been broken down!!"
        jump que_done
    label que_2:
        voice"nar/p8.MP3"
        n "uhh.. you straight up leave"
        voice"nar/p9.MP3"
        n " well i guess you did"
        voice"nar/p12.MP3"
        n "why tho??"
        voice"nar/p11.MP3"
        n "anyways back in the hall"
        jump que_done
    label que_3:
        voice"nar/p13.MP3"
        n "seamus the mouse must not care much for security"
        voice"nar/d1.MP3"
        n " the keypad only has two dijts"
        menu:
            "you press the digit 1":
                jump bo_oh
            "you press the digit two":
                jump bo_no
        label bo_oh:
            voice"nar/b1.MP3"
            n " you hear some whirring and then "
            voice"nar/b2.MP3"
            n " the whole key pad comes off!"
            voice"nar/b3.MP3"
            n " you spot a key inside of the key pad"
            jump bo_done
        label bo_no:
            voice"nar/j1.MP3"
            n " after pressing two you realize nothing had happened (noooo)"
            voice"nar/j2.MP3"
            n " so you press one "
            voice"nar/b1.MP3"
            n " you hear some whirring and then "
            voice"nar/b2.MP3"
            n " the whole key pad comes off!"
            voice"nar/b3.MP3"
            n " you spot a key inside of the key pad"
            jump bo_done
        label bo_done:
        voice"nar/j3.MP3"
        n "you use the key to open the door (yeet)"
        voice"nar/j4.MP3"
        n "yay! "
        voice"nar/j5.MP3"
        d "creak"
        voice"nar/j6.MP3"
        n " the door opened!"
        jump que_done
    label que_done:

    scene wer
    voice"nar/z1.MP3"
    n " you see seamus ..."
    voice"nar/z2.MP3"
    n " And teh generic kidnapped kid!!!"
    voice"nar/z3.MP3"
    n " peacefully eating cheze and talking"
    voice"nar/z4.MP3"
    n "as you approach them you hear them talking"
    voice"huz/j1.MP3"
    a "so how are we going to get you back to yer parents"
    voice"huz/m1.MP3"
    b "i sobs dunno sobs"
    voice"huz/j2.MP3"
    a "i met you in the midddle of the sewer"
    voice"huz/j8.MP3"
    a " how on earth did you get there?"
    voice"huz/sobs.MP3"
    b "i sobs dunno sobs"
    voice"huz/j9.MP3"
    a " do you have any idea where your very generic family is?"
    voice"huz/sob2.MP3"
    b "i sobs dunno sobs your cheze is weird sobs"
    voice"huz/j19.MP3"
    a " Whats wrong with meh cheze?!?"
    voice"nar/z5.MP3"
    n "you decide to talk to them"
    voice"you/o2.MP3"
    y " hello fellow creatures"
    voice"you/o10.MP3"
    y " with the power of the narrator and anime on my side!!!"
    voice"you/ohmy.MP3"
    y " i can bring sad generic kid back to his family"
    voice"huz/yeayi.MP3"
    a " yay "
    voice"huz/yaysob.MP3"
    b " yay sobs"
    voice"nar/z6.MP3"
    n "in some very quick scenes"
    scene dud
    r " "
    voice"nar/mum.MP3"
    u "with no explanation why they happened"
    r " "
    scene tfr
    r " "
    scene run
    voice"nar/z7.MP3"
    n " you reunited the family"
    scene ent
    voice"you/o1.MP3"
    y "yay "
    voice"huz/yaysob.MP3"
    b "yay sobss"
    voice"you/c5.MP3"
    p "thanks yous sos muchs sobs"
    voice"nar/z8.MP3"
    n "then you decide to deliver that package to neil"
    voice"nar/z9.MP3"
    n "you go down the hallway"
    scene ding
    voice"nar/z10.MP3"
    n "(you see neil) and he starts talking to you"
    voice"shelly/d1.MP3"
    g "Happy GroundHog day!"
    voice"shelly/d2.MP3"
    g "thanks for the package"
    voice"nar/z19.MP3"
    n "after getting over neil's terrible charecter design,"
    voice"nar/z20.MP3"
    n "you realize that Neil has taken the package"
    voice"nar/neila.MP3"
    n "(neil gives you apple)"
    voice"shelly/d5.MP3"
    g "Here's some apples for a fellow groundhog."
    voice"shelly/d7.MP3"
    g "i love apples"
    voice"shelly/d9.MP3"
    g "even more than"
    voice"shelly/guo.MP3"
    scene chiners
    voice"shelly/d0.MP3"
    g "a realy abrupt scene change"
    voice"nar/lolol.MP3"
    n "lol"
    voice"nar/yayfin.MP3"
    n "thanks for playing!!! huzahhh!!!"
    voice"nar/eroe.MP3"
    r "and now itz time for credits!!!"
    play music "audio/yussss.mp3"
    scene img
    show o at truecenter
    ""
    show s at truecenter
    ""
    show c at truecenter
    ""
    show t at truecenter
    ""
    show j at truecenter
    ""
    show g at truecenter
    ""
    show m at truecenter
    ""
    show n at truecenter
    ""
    show k at truecenter
    ""
    show chiners
    ""








        # ... the game continues here.
