import random
from faker import Faker
from first_app.models import Topico,Webpage,RegistroAcesso

fakegen = Faker()
topics = ['Pesquisa', 'Social', 'Marketplace', 'Noticias', 'Jogos']


def add_topic():
    t = Topico.objects.get_or_create(nome=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        top = add_topic()

        url = fakegen.url()
        data = fakegen.date()
        nome = fakegen.company()

        pagina = Webpage.objects.get_or_create(topico=top, url=url, nome=nome)[0]

        _ = RegistroAcesso.objects.get_or_create(pagina=pagina, data=data)[0]

print("Populando o banco de dados")
populate(20)

