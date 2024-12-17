import flet as fl

def main(page: fl.Page):
  BG = '#051751'
  FWG = '#7991DF'
  FG = '#374E9D'
  PINK = '#D900F4'
  
  categories_card = fl.Row(
    scroll='auto'
  )
  categories = ['Business', 'Family', 'Friends', 'Health']
  for category in categories:
    categories_card.controls.append(
      fl.Container(
        bgcolor=BG, 
        height=110, 
        width=170,
        border_radius=20,
        padding=15
      )
    )
  
  
  first_page_contents = fl.Container(
    content=fl.Column(
      controls=[
        fl.Row(alignment='spaceBetween',
          controls=[
            fl.Container(bgcolor='#2D2D2D', # убрать
              content=fl.Icon(
                fl.icons.MENU
              )
            ),
            fl.Row(
              controls=[
                fl.Icon(fl.icons.SEARCH),
                fl.Icon(fl.icons.NOTIFICATIONS_OUTLINED)
              ]
            )
          ]
        ),
        fl.Container(height=20, bgcolor='#E5BD39'),
        fl.Text(
          value='What\'s up, George!'
        ),
        fl.Text(
          value='CATEGORIES'
        ),
        fl.Container(
          padding=fl.padding.only(top=10, bottom=20, ),
          bgcolor='#DF6D49',
          content=categories_card
         ),
      ]
    ), bgcolor='#CE7CA0' # убрать
  )

  page_1 = fl.Container()
  page_2 = fl.Row(
    controls=[
      fl.Container(
        width=400,
        height=850,
        bgcolor='#9A012D', # убрать
        border_radius=35,
        padding=fl.padding.only(
          top=50, left=20, right=20, bottom=5
        ),
        content=fl.Column(
          controls=[
            first_page_contents
          ]
        )
      )
    ]
  )
  
  container = fl.Container(
    width=500, 
    height=850, 
    bgcolor=BG, 
    border_radius=35,
    content=fl.Stack(
      controls=[
        page_1,
        page_2
      ]
    )
    )
  page.add(container)


fl.app(target=main)

#ОСТАНОВИЛСЯ НА 21:31 в видео