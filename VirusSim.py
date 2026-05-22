import time
import play
import random

simulation_started = False
ziekenhuis_aan = True
vaccinatie_aan = True

#start sprites
start_knop = play.new_box(
    x=0,
    y=80,
    width=200,
    height=100,
    color="red",
    border_color="green",
    border_width=4
)

start_tekst = play.new_text(
    words="START",
    x=0,
    y=80,
    font_size=40,
    color="black"
)

start_tekst2 = play.new_text(
    words="Virus Simulatie",
    x=0,
    y=190,
    font_size=40,
    color="black"
)

Start_afbeelding = play.new_image(
    'Virus.png',
    x=290,
    y= 70,
    size= 60
)

Start_afbeelding2 = play.new_image(
    'Virus.png',
    x=-290,
    y= 70,
    size= 60
)

gekozen_aantal = 20

knop20 = play.new_box(
    x=-220,
    y=-120,
    width=120,
    height=60,
    color="lightgreen",
    border_color="black",
    border_width=2
)

tekst20 = play.new_text(
    words="20",
    x=-220,
    y=-120,
    font_size=30,
    color="black"
)

knop50 = play.new_box(
    x=0,
    y=-120,
    width=120,
    height=60,
    color="white",
    border_color="black",
    border_width=2
)

tekst50 = play.new_text(
    words="50",
    x=0,
    y=-120,
    font_size=30,
    color="black"
)

knop100 = play.new_box(
    x=220,
    y=-120,
    width=120,
    height=60,
    color="white",
    border_color="black",
    border_width=2
)

tekst100 = play.new_text(
    words="100",
    x=220,
    y=-120,
    font_size=30,
    color="black"
)

keuzeTekst = play.new_text(
    words="Aantal Personen",
    x=0,
    y=-60,
    font_size=30,
    color="black"
)

# ziekenhuis knop
ziekenhuis_knop = play.new_box(
    x=-150,
    y=-200,
    width=180,
    height=60,
    color="lightgreen",
    border_color="black",
    border_width=2
)

ziekenhuis_knop_tekst = play.new_text(
    words="Ziekenhuis: AAN",
    x=-150,
    y=-200,
    font_size=22,
    color="black"
)

# vaccinatie knop
vaccinatie_knop = play.new_box(
    x=150,
    y=-200,
    width=180,
    height=60,
    color="lightgreen",
    border_color="black",
    border_width=2
)

vaccinatie_knop_tekst = play.new_text(
    words="Vaccinatie: AAN",
    x=150,
    y=-200,
    font_size=22,
    color="black"
)


class Persoon():
    def __init__(self,status,kleur):
        self.color = kleur
        self.status = status
        self.ziekteDuur = 0 

        self.object = play.new_circle(
            x=random.randint(-350,350), 
            y=random.randint(-250,250), 
            radius=15, 
            color=self.color
        )
        
        vy = random.randint(-100,100)
        vx = random.randint(-100,100)  
    
        self.object.start_physics(
            can_move=True, 
            stable=False, 
            x_speed=vx, 
            y_speed=vy,
            obeys_gravity=False, 
            bounciness=5, 
            mass=10, 
            friction=0
        )

    def setKleur(self):
        self.object.color = self.color

    def maakZiek(self, current_time):
        self.color = "red"
        self.setKleur()
        self.status = "Viral"
        self.ziekteDuur = current_time


personen = []

begintijd = time.time()

tijdInBeeld = play.new_text(
    words='0',
    x=350,
    y=250,
    font_size=30,
    color='black',
)

# ziekenhuis
ziekenhuis = play.new_box(
    x = -330,
    y = 250,
    width = 140,
    height = 100,
    color = "lightblue",
    border_color = "blue",
    border_width = 3
)

ziekenhuisTekst = play.new_text(
    words="Ziekenhuis",
    x=-330,
    y=250,
    font_size=20,
    color="black"
)

# vaccinatie
vaccinatie = play.new_box(
    x = 330,
    y = 250,
    width = 160,
    height = 100,
    color = "plum",
    border_color = "purple",
    border_width = 3
)

vaccinatieTekst = play.new_text(
    words="Vaccinatie",
    x=330,
    y=250,
    font_size=20,
    color="black"
)


#verbergen op start
ziekenhuis.hide()
ziekenhuisTekst.hide()
vaccinatie.hide()
vaccinatieTekst.hide()

@play.repeat_forever
async def check_start():

    global simulation_started
    global begintijd
    global gekozen_aantal

    if not simulation_started:
        
        # knop 20
        if knop20.is_clicked:
            gekozen_aantal = 20
            knop20.color = "lightgreen"
            knop50.color = "white"
            knop100.color = "white"
        
        # knop 50
        if knop50.is_clicked:
            gekozen_aantal = 50
            knop20.color = "white"
            knop50.color = "lightgreen"
            knop100.color = "white"

        # knop 100
        if knop100.is_clicked:
            gekozen_aantal = 100
            knop20.color = "white"
            knop50.color = "white"
            knop100.color = "lightgreen"

        global ziekenhuis_aan
        global vaccinatie_aan

        # ziekenhuis knop
        if ziekenhuis_knop.is_clicked:

            ziekenhuis_aan = not ziekenhuis_aan

            if ziekenhuis_aan:
                ziekenhuis_knop.color = "lightgreen"
                ziekenhuis_knop_tekst.words = "Ziekenhuis: AAN"
            else:
                ziekenhuis_knop.color = "lightcoral"
                ziekenhuis_knop_tekst.words = "Ziekenhuis: UIT"


        # vaccinatie knop
        if vaccinatie_knop.is_clicked:

            vaccinatie_aan = not vaccinatie_aan

            if vaccinatie_aan:
                vaccinatie_knop.color = "lightgreen"
                vaccinatie_knop_tekst.words = "Vaccinatie: AAN"
            else:
                vaccinatie_knop.color = "lightcoral"
                vaccinatie_knop_tekst.words = "Vaccinatie: UIT"

        if start_knop.is_clicked:

            simulation_started = True

            start_knop.hide()
            start_tekst.hide()
            start_tekst2.hide()
            Start_afbeelding.remove()
            Start_afbeelding2.remove()    

            knop20.hide()
            knop50.hide()
            knop100.hide()
            tekst20.hide()
            tekst50.hide()
            tekst100.hide()
            keuzeTekst.hide()
            ziekenhuis_knop.hide()
            ziekenhuis_knop_tekst.hide()
            vaccinatie_knop.hide()
            vaccinatie_knop_tekst.hide()
            
            if ziekenhuis_aan:
                ziekenhuis.show()
                ziekenhuisTekst.show()
                

            # toon vaccinatie alleen als aan
            if vaccinatie_aan:
                vaccinatie.show()
                vaccinatieTekst.show()


            begintijd = time.time()

            # gezonde personen
            for count in range(gekozen_aantal - 1):
                personen.append(Persoon('Healthy','green'))

            # besmet persoon
            for count in range(1):
                personen.append(Persoon('Viral','red'))

            current_time = time.time()
            personen[-1].ziekteDuur = current_time
    
    

@play.repeat_forever
async def viruscheck():

    if not simulation_started:
        return

    current_time = time.time()

    for persoon1 in personen[:]:


        # ziekenhuis
        if ziekenhuis_aan:
            if persoon1.object.is_touching(ziekenhuis):

                if persoon1.status == "Viral":
                    persoon1.color = "blue"
                    persoon1.setKleur()
                    persoon1.status = "Healthy"
                    persoon1.ziekteDuur = 0

        # vaccinatie
        if vaccinatie_aan:
            if persoon1.object.is_touching(vaccinatie):

                if persoon1.status == "Healthy" or persoon1.status == "Masked":
                    persoon1.color = "purple"
                    persoon1.setKleur()
                    persoon1.status = "Resistant"

        # na 20 seconden sterft besmet persoon
            if current_time - persoon1.ziekteDuur > 20 and persoon1.status == "Viral":
                persoon1.color = "black"
                persoon1.setKleur()
                persoon1.status = "Dead"

                # stoppen bewegen
                persoon1.object.physics.x_speed = 0
                persoon1.object.physics.y_speed = 0
                persoon1.object.physics.can_move = False


        # masker
        if persoon1.object.is_clicked and persoon1.status == "Viral":
            persoon1.color = "orange"
            persoon1.setKleur()
            persoon1.status = "Masked"


        for persoon2 in personen[:]:

            if persoon1 == persoon2:
                continue

            
            if persoon1.object.distance_to(persoon2.object) < (
                persoon1.object.radius + persoon2.object.radius + 13
            ):

                if ((persoon1.status == "Viral") ^ (persoon2.status == "Viral")):

                    if persoon1.status == "Resistant" or persoon2.status == "Resistant":
                        continue
                    
                    kans = play.random_number(0,100)

                    if persoon1.status == "Viral" and persoon2.status == "Healthy" and kans <= 80:
                        persoon2.maakZiek(current_time)

                    if persoon2.status == "Viral" and persoon1.status == "Healthy" and kans <= 80:
                        persoon1.maakZiek(current_time)

                    if persoon1.status == "Viral" and persoon2.status == "Masked" and kans <= 20:
                        persoon2.maakZiek(current_time)

                    if persoon2.status == "Viral" and persoon1.status == "Masked" and kans <= 20:
                        persoon1.maakZiek(current_time)

                    persoon1.object.physics.x_speed *= -1
                    persoon1.object.physics.y_speed *= -1

                    persoon2.object.physics.x_speed *= -1
                    persoon2.object.physics.y_speed *= -1


    iedereenBesmet = True

    for persoon1 in personen:
        if persoon1.status == "Healthy":
            iedereenBesmet = False

    geenBesmettePersonen = True

    for persoon1 in personen:
        if persoon1.status == "Viral":
            geenBesmettePersonen = False


    if (iedereenBesmet or geenBesmettePersonen) and len(personen) > 0:
        eindtijd = round(time.time() - begintijd)
        tijdInBeeld.words = eindtijd
        await play.timer(seconds=1)

        aantal_gezond = 0
        aantal_besmet = 0
        aantal_dood = 0
        aantal_gevaccineerd = 0

        for persoon in personen:

            if persoon.status == "Healthy" or persoon.status == "Masked":
                aantal_gezond += 1

            elif persoon.status == "Viral":
                aantal_besmet += 1

            elif persoon.status == "Dead":
                aantal_dood += 1

            elif persoon.status == "Resistant":
                aantal_gevaccineerd += 1

        f = open("simulatie.txt", "a")

        f.write("Tijd: " + str(eindtijd) + " seconden\n")
        f.write("Gezond: " + str(aantal_gezond) + "\n")
        f.write("Besmet: " + str(aantal_besmet) + "\n")
        f.write("Dood: " + str(aantal_dood) + "\n")
        f.write("Gevaccineerd: " + str(aantal_gevaccineerd) + "\n")
        f.write("-------------------------\n")

        f.close()

        print(eindtijd)
        exit()


play.start_program()