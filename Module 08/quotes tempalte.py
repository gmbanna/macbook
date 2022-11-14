"""
aladin says. i have

"""

quotes = [
{
"anime": "Psycho-Pass",
"character": "Oryou Rikako",
"quote": "Everyone here is the same. They don't notice anything. They don't say anything. And they don't think anything. They are merely a shell of their former selves and soon they will disappear like the melting snow. This epidemic leads innocent people to their deaths, and yet, its pathogen will never be eradicated. This is a disease called serenity - a form of death that people have wished for."
},
{
"anime": "Kaichou Wa Maid-Sama!",
"character": "Takumi Usui",
"quote": "How far do you want me to suppress myself so that you'll be satisfied?"
},
{
"anime": "The World God Only Knows",
"character": "Keima Katsuragi",
"quote": "Does the world hate me or something? I've always rejected it in an exceedingly friendly manner."
},
{
"anime": "Shirobako",
"character": "Midori Imai",
"quote": "I just realized I love learning things that I don't know anything about. It sort of feels like I'm one step closer to my dream."
},
{
"anime": "Yu-Gi-Oh! Arc-V",
"character": "Reiji Akaba",
"quote": "No matter how careful your risk hedging is, there will still be holes in your plan! Realizing them and making sure that they are promptly dealt with, is the duty of those who stand at the top."
},
{
"anime": "Shigatsu Wa Kimi No Uso",
"character": "Kaori Miyazono",
"quote": "Maybe there’s only a dark road up ahead. But you still have to believe and keep going. Believe that the stars will light your path, even a little bit."
},
{
"anime": "Avatar: The Last Airbender",
"character": "Roku",
"quote": "If I had been more decisive, and acted sooner, I could have stopped Sozin, and stopped the war before it started. I offer you this wisdom, Aang, you must be decisive."
},
{
"anime": "Danganronpa: Kibou No Gakuen To Zetsubou No Koukousei",
"character": "Ludenberg Celestia",
"quote": "It is not the strong or the smart that survive, but the ones who can bring about change."
},
{
"anime": "Naruto",
"character": "Hatake Kakashi",
"quote": "Hmmm...how do I put this? My first impression of this group...you're a bunch of idiots!"
},
{
"anime": "Bleach",
"character": "Kuchiki Byakuya",
"quote": "Are you telling me to exploit an opening for the likes of you? Do not speak out of your league, boy."
}
]

# print(type(quotes))

for quote in quotes:
    character = quote.get('character')
    q = quote.get('quote')

    template = f'{character} says, "{q}"'

    print(template)
    print('*' * 10)


