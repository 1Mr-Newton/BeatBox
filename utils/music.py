from flet import *

class Music(UserControl):
  def __init__(self,artist,cover_art,title,length,streams,like,num):
    super().__init__()
    mtc = '#ceced0'
    tnc = '#c3c9d2'
    self.artist =artist
    self.cover_art = cover_art
    self.title = title
    self.length = length
    self.streams = streams
    self.like = like
    self.num = num
    self.tnc = tnc
    self.mtc = mtc
    self.play_pause_btn = Container(
      on_hover=self.play_hover,
      width=50,height=50,border_radius=30,
      content=Icon(icons.PLAY_ARROW,color='black')
    )
    self.main_container = Container(on_hover=self.main_hover,
          padding=padding.only(top=2,bottom=2, left=10,right=10),
          height=70,
          width=620,
          border_radius=20,
          content=Row(
            vertical_alignment='center',
            alignment='spaceBetween',
            controls=[
              Container(
                width=30,
                content=Text(
                  value=self.num,
                  size=22,
                  color=self.tnc
                ),
              ),
              Container(
                clip_behavior=ClipBehavior.ANTI_ALIAS,
                height=60,
                width=60,
                border_radius=16,
                content=Image(
                  src=f'assets/cover_arts/{self.cover_art}',
                  fit=ImageFit.COVER
                )
              ),
              Container(
                clip_behavior=ClipBehavior.ANTI_ALIAS,
                width=200,
                content=Column(
                  alignment='center',
                  spacing=5,
                  controls=[
                    Text(
                      value=self.title,
                      font_family='SF Pro Semibold',
                      color='black',
                      size=15,
                      no_wrap=True,
                      tooltip=self.title
                    ),
                    Row(
                      controls=[
                        Icon(
                          icons.PERSON,
                          color=self.tnc,
                          size=10
                        ),
                        Text(
                          value=self.artist,
                          font_family='SF Pro Semibold',
                          color=self.tnc,
                          size=10,
                          no_wrap=True
                        ),
                      ]
                    )
                  ]
                )
              ),
              Container(
                width=60,
                content=Text(
                  value=self.length,
                  color='black',
                  font_family='SF Pro Heavy',
                  size=12,
                ),
              ),
              self.play_pause_btn,
              Container(
                width=30,
                content=Icon(
                  icons.FAVORITE_OUTLINE,
                  color='black',
                )
              ),
              Container(
                width=20,
                content=Row(
                  spacing = 3,
                  controls=[
                    Container(
                      height=4,
                      width=4,
                      bgcolor='black',
                      border_radius=5
                    ),
                    Container(
                      height=4,
                      width=4,
                      bgcolor='black',
                      border_radius=5
                    ),
                    Container(
                      height=4,
                      width=4,
                      bgcolor='black',
                      border_radius=5
                    ),
                  ]
                )
              ),
            ]
          )
        )
  def main_hover(self,e):
    if e.data == 'true':
      self.main_container.bgcolor = '#fefefe'         
      self.main_container.update()
    else:  
      self.main_container.bgcolor = None
      self.main_container.update()

  def play_hover(self,e):
    if e.data == 'true':
      self.play_pause_btn.bgcolor = 'black12'
      self.play_pause_btn.update()
    else:
      self.play_pause_btn.bgcolor = None
      self.play_pause_btn.update()  

  def build(self):
    return Column(
      controls=[
        self.main_container,                     
      ]
    )  