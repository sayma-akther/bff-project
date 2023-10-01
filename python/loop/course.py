course_list=[
    {
        "name":"Sayma",
        "i_have_enrolled":"Python And Web",
        "i_have_learned":"html, css, bootstrap, python"
    },
   
    {
        "name":"Sayma",
        "i_have_enrolled":"java Spring Boot",
        "i_have_learned":"java, html, css, js"
    },
    {
        "name":"Sayma",
        "i_have_enrolled":"PHP and Wordpress",
        "i_have_learned":"PHP, html, css, js, WOrdpress theme"
    },

    {
        "name":"Sayma",
        "i_have_enrolled":"Web Front-End Development",
        "i_have_learned":"html, css, js, Typescript, React"
    }

]

for item in course_list:
    print()
    for key, value in item.items():
        print(f"{key} : {value}")