events = (
    { 
        "type": "matutino", 
        "days": [
            { 
                "name": "segunda-feira",
                "course_name": "Criar e contar histórias",
                "series": [2, 3],
            },
            { 
                "name": "terça-feira",
                "course_name": "Teatro: Luz, câmera e ação",
                "series": [3, 4]
            },
            { 
                "name": "quarta-feira",
                "course_name": "A língua de sinais",
                "series": [2, 3, 4, 5]
            },
            { 
                "name": "quinta-feira",
                "course_name": "Expressão Artística",
                "series": [4, 5]
            },
            { 
                "name": "sexta-feira",
                "course_name": "Soletrando",
                "series": [5]
            },
        ] 
    },
    { 
        "type": "vespertino", 
        "days": [
            {
                "name": "segunda-feira",
                "course_name": "Leitura dramática",
                "series": [4]
            },
            { 
                "name": "terça-feira",
                "course_name": "O corpo fala",
                "series": [3]
            },
            { 
                "name": "quarta-feira",
                "course_name": "O mundo da imaginação",
                "series": [2]
            },
            { 
                "name": "quinta-feira",
                "course_name": "Leitura dinâmica",
                "series": [5]
            },
            { 
                "name": "sexta-feira",
                "course_name": "Criando e recriando com emojis",
                "series": [2]
            },
        ] 
    },
)
studentList = []
eventsRegistration = []

# Função que chama o menu de opções
def menu(alreadyDone): 
    print("-"*50)
    print("COLEGIO NOVA ESPERANÇA-EVENTO LITERARIO")
    print("-"*50)
    print(" ")
    print("***Menu de Opções***")
    if alreadyDone == 0:
        print("1- Cadastrar Alunos")
    print("2- Fazer Inscrições")
    print("3- Listar Inscrições")
    print("4- Sair")
    print("********************")

    # Entrada de dados pelo usuário para começar a lógica do programa
    return int(input("Escolha a opção desejada, apenas o numero: "))

# Retorna o aluno de acordo com o RM
def getStudentByRm(rm):
    if len(studentList) > 0:
        exist = [x for x in studentList if x['rm'] == rm]
        if exist:
            return exist[0]
    
    return

# Verifica se a serie informanda está dentro do range definido
def existSerie(serie):
    return serie < 2 or serie > 5

# Registra os alunos na listagem
def studentsRegistration(): 
    while True:
        
        # Receber os rms para registro
        rm = int(input("Digite o rm do aluno: "))
        
        # Verifica se o rm informando é igual a 0, caso sim, sair do fluxo de cadastro
        if rm == 0:
            break
        elif rm != 0:
            #  Verifica se existe um aluno com o mesmo RM
            if getStudentByRm(rm):
                print("Rm ja existente!")
            else: 
               #validando se a serie existe 
                studentClass = int(input("Digite a serie em que o aluno se encontra, apenas numero: "))
                while existSerie(studentClass):
                    print("Série não encontrada!")
                    print("Só estão válidas da 2 a 5 serie!")
                    studentClass = int(input("Digite  a série do aluno: "))
                
                # Capturando nome do aluno
                studentName = input("Digite o nome do aluno: ")
                studentList.append({ "rm": rm, "name": studentName, "serie": studentClass, "course_count": 0 })
                print("--Aluno Cadastrado--")
                print("--Proximo Aluno--")

# Retorna os eventos disponíveis por série
def getListEventBySerie(serie): 
    listEventAvailable = [
        {
            "type": "matutino",
            "courses": []
        },
        {
            "type": "vespertino",
            "courses": []
        },
    ]

    idItem = 1
    for item in events:
        for day in item["days"]:
            if serie in day["series"]:
                existCourse = [x for x in eventsRegistration if x['course_name'] == day["course_name"]]
                if len(existCourse) <= 0 or existCourse[0]["count"] < 10:
                    avaliableItem = [x for x in listEventAvailable if x['type'] == item["type"]]

                    # Verificando a quantidade de vagas disponíveis
                    avaliable_count = 10
                    if len(existCourse) > 0:
                        avaliable_count = 10 - existCourse[0]["count"]
                    
                    avaliableItem[0]["courses"].append({
                        "id": idItem,
                        "course_name": day["course_name"],
                        "day_name": day["name"],
                        "avaliable_count": avaliable_count,
                        "type": item["type"],
                    })
                    idItem+=1

    return listEventAvailable

# Realiza as inscrição dos alunos nas oficinas
def studentsSubscribe():
    print("")
    print("-"*50)
    print("REALIZANDO INSCRIÇÕES")
    print("-"*50)
    
    # Validando se o rm já foi cadastrado
    rm = int(input("Digite seu rm: "))
    if getStudentByRm(rm):
        
        # Buscar o aluno desse rm
        student = getStudentByRm(rm)
        
        # Verificar se esse aluno possui permissão para add mais eventos
        if student["course_count"] == 3:
            print("O aluno(a) " + student["name"] + " já está cadastrado em 3 eventos.")
            return

        # Oficinas disponiveis para esse aluno
        listEventAvaliable = getListEventBySerie(student["serie"])
        print("As oficinas disponíveis para o aluno(a) " + student["name"] + " são as seguintes:")
        for item in listEventAvaliable:
            print("-"*50)
            print("")
            print(item["type"])
            for itemType in item["courses"]:
                print(str(itemType["id"]) + "- " + itemType["day_name"] + " - " + itemType["course_name"] + " - " + str(itemType["avaliable_count"]) + " disponíveis")
            print("")  

        # Escolhendo o evento para add no aluno
        courseId = int(input("Digite o número do curso: "))
        course = []
        itemVerify = 0
        while len(course) <= 0:
            course = [x for x in listEventAvaliable[itemVerify]["courses"] if x['id'] == courseId]
            itemVerify+=1

        # Pegando o item de evento registrado
        existCountName = [x for x in eventsRegistration if x['course_name'] == course[0]["course_name"]]

        # Verificar se o aluno já está cadastrado nesse evento
        if len(existCountName) > 0 and student["rm"] in existCountName[0]["listStudents"]:
            print("O aluno(a) " + student["name"] + " já está cadastrado neste evento.")
            return

        # Add o usuário no evento
        if existCountName: # Se já tiver o curso na lista, add o numero de count
            existCountName[0]["count"]+=1
            existCountName[0]["listStudents"].append(student["rm"])
        else: # Se não, a gente add na lista 
            eventsRegistration.append({
                "course_name": course[0]["course_name"],
                "count": 1,
                "listStudents": [student["rm"]],
                "day_name": course[0]["day_name"],
                "type": course[0]["type"]
            })
        student["course_count"]+=1
    else: # caso aluno nao esteja cadastrado, vai voltar ao menu de opções
        print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I") 

# Retorna a lista de estudantes com ordenação pelo nome
def listStudentsByName():
    
    # Ordenando a listagem pelo nome
    listStudentWithCourse = sorted(studentList, key=lambda x: (x["name"], x["name"]))
    
    # Passar por cada aluno e informar qual os cursos de cada um
    for student in listStudentWithCourse:
        student["courses"] = []
        for event in eventsRegistration:
            if student["rm"] in event["listStudents"]:
                student["courses"].append({
                    "name": event["course_name"],
                    "day_name": event["day_name"],
                    "type": event["type"],
                })

    # Printando os students 
    print("")
    print("Alunos inscritos - ordem alfabéticas(nome): ")
    for student in listStudentWithCourse:
        print("RM: " + str(student["rm"]) + "- " + student["name"] + " - " + str(student["serie"]) + " série")
        print("Oficinas: ")
        for event in student["courses"]:
            print(event["type"] + " - " + event["name"] + " - "+ event["day_name"])
        print("")

# Retorna a lista de eventos com ordenação pelo nome
def listEventsByName():

    # Criando lista dos eventos existentes
    listEventsWithStudents = []
    for item in events:
        for day in item["days"]:
            listEventsWithStudents.append({
                "type": item["type"],
                "course_name": day["course_name"],
                "day_name": day["name"],
                "listStudents": []
            })

    # Ordenando a listagem pelo nome
    listEventsWithStudents = sorted(listEventsWithStudents, key=lambda x: (x["course_name"], x["course_name"]))

    # Verificando se o aluno faz parte desse curso
    for event in listEventsWithStudents:

        # Procurar esse evento no eventsRegistration
        exist = [x for x in eventsRegistration if x['course_name'] == event["course_name"]]
        if len(exist) > 0:
            # Verifica quais os alunos que estão presente
            for rm in exist[0]["listStudents"]:
                student = getStudentByRm(rm)
                event["listStudents"].append(student)

    # Printando a listagem de oficinas
    print("")
    print("Oficinas - ordem alfabéticas(nome): ")
    for event in listEventsWithStudents:
        print(event["course_name"] + " - " + event["day_name"] + " - " + event["type"])
        print("Alunos: ")
        for student in event["listStudents"]:
            print("RM: " + str(student["rm"]) + "- " + student["name"] + " - " + str(student["serie"]) + " série")
        print("Total: " + str(len(event["listStudents"])) + " alunos")
        print("")

# Menu de opção para as listagens
def listRegistration():
    print("")
    print("-"*50)
    print("LISTA DE INSCRIÇÕES")
    print("-"*50)
    print("1 - Listar por aluno (ordem alfabética de nome)")
    print("2 - Listar por oficina (ordem alfabética)") 
    print("0 - Voltar para o menu")
    op = int(input("Selicione uma opção: "))
    while op <0 or op > 2:
        print("Opção inválida!")
        op = int(input("Digite uma opção válida: "))
    if op == 0:
        return
    elif op == 1:
        listStudentsByName()
    elif op == 2:
        listEventsByName()

# Iniciando o sistema
alreadyDone = 0
while alreadyDone == 0:
    # Atribuir um controle de acesso ao menu
    while True:
        option = menu(alreadyDone)
        while option < 1 or option > 4:
            print("Opção invalida!")
            option = int(input("Digite uma opção valida: "))
        if option == 1 and alreadyDone == 0:
            studentsRegistration()
            alreadyDone+=1
        elif option == 2:
            studentsSubscribe()
        elif option == 3:
            listRegistration()
        elif option == 4:
            break
