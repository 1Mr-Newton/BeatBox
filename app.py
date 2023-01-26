from mutagen.mp3 import MP3
from utils.music import Music
from flet import *
import asyncio
from utils.music import Music
sb = '#f9373658'
mb = '#f9463760'
pc = '#131939'
ac = '#1d2237'
hb = '#f9fafafe'
sbc = '#ffffff'
mtc = '#ceced0'
tnc = '#c3c9d2'
ic = '#61265a'
sbic = '#9c9db6'
w = 1200
h = 870
audio_url = 'assets/audio/africaq.mp3'
class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg
    self.pick_files_dialog = FilePicker(on_result=self.load_songs)
    self.init_helper()
    self.load_songs_onstart()

  def init_helper(self):
    self.song_obj = Music
    self.music_library_column = self.music_library_column()
    self.playlist_obj =self.playlist_obj() 
    self.playlists_row = self.playlists_content()
    self.audio_url = audio_url
    self.sidebar_content_handler = self.sidebar_content_handler()
    self.audio_dur = self.audio_dur()
    self.audio_cur_pos = self.audio_cur_pos()
    self.song_title = self.song_title()
    self.audio_progress = self.audio_progress()
    self.cover_art = self.cover_art()
    self.sidebar_btns_loader()

    
    self.artist_name = self.artist_name()
    self.audio_player_details = self.audio_player_details()
    self.audio_playtime_and_indicator = self.audio_playtime_and_indicator()
    self.audio_player = self.audio_player()
    self.page_1 = self.base_layout()
    self.page_2 = self.page2()
    self._main = self.base()
    # 
    self.pg.fonts = {
      "SF Pro Bold":"fonts/SFProText-Bold.ttf",
      "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
      "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
      "SF Pro Light":"fonts/SFProText-Light.ttf",
      "SF Pro Medium":"fonts/SFProText-Medium.ttf",
      "SF Pro Regular":"fonts/SFProText-Regular.ttf",
      "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
      "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    }
    self.pg.window_bgcolor = colors.TRANSPARENT
    self.pg.bgcolor = colors.TRANSPARENT
    self.pg.window_title_bar_hidden = True
    self.pg.window_frameless = True
    self.pg.window_height =h 
    self.pg.window_width = w
    self.audio1 = self.audio1()
    self.pg.overlay.append(self.audio1)
    self.pg.overlay.append(self.pick_files_dialog)
    
    
    
    self.pg.add(self.base())


  def base(self):
    return Container(
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      width=w,
      expand=True,
      border_radius=35,
      content=self.main_frame()
    )  
    
  def main_frame(self):
    return Stack(
      controls=[
        self.page_1,
        self.page_2,
      ]

    )  
  

  def shrink(self,e):
    self.page_1.controls[0].width = 700
    self.page_1.controls[0].opacity = 0.2
    self.page_1.update()

  
  def restore(self,e):
    self.page_1.controls[0].width = w
    self.page_1.controls[0].opacity = 1
    self.page_1.update()

  def music_library_column(self):
    return Column(
      scroll='auto',
      controls=[
        self.song_obj(artist='Mr. Newton ft Dj Divomi',cover_art='africaq.jpg',title='Coding na your mate?',length='3:12',streams="24,214,102",like=False,num='01'),
      ]
    )
  
  def page2c(self):
    return Container(
    content=Column(
      controls=[
        Row(alignment='spaceBetween',
          controls=[
            Container(
              on_click=lambda e: self.shrink(e),
              content=Icon(
                icons.MENU)),
            Row(
              controls=[
                Icon(icons.SEARCH),
                Icon(icons.NOTIFICATIONS_OUTLINED),
              ],
            ),
          ],
        ),
        Container(height=20),
        Text(
          value='What\'s up, Olivia!'
        ),
        Text(
          value='CATEGORIES'
        ),
        Container(
          padding=padding.only(top=10,bottom=20,),
          content=Container()
        ),
        Container(height=20),
        Text("TODAY'S TASKS"),
        Stack(
          controls=[
            # tasks,
            FloatingActionButton(bottom=2,right=20,
              icon = icons.ADD,on_click=lambda _: page.go('/create_task')
            )
          ]
        )
      ],
    ),
  )
  
  
  def page2(self):
    return Row(alignment='end',
    controls=[
      Container(
        padding=8,
        height=850,
        width=700,
        content=Container(
          padding=padding.only(left=30,right=30),
          expand=True,
          border_radius=35,
          bgcolor=hb,
          content=Column(
            controls=[
              WindowDragArea(content=Container(height=30)),
              Row(
                alignment='spaceBetween',
                controls=[
                  Text(
                    value="Home",
                    font_family='SF Pro Semibold',
                    color='black',
                    size=40,
                  ),
                  Row(
                    controls=[
                      Icon(icons.NOTIFICATIONS_OUTLINED,color='black'),
                      Container(
                        clip_behavior=ClipBehavior.ANTI_ALIAS,
                        bgcolor=sbc,
                        width=280,
                        height=40,
                        padding=padding.only(left=10,right=8,top=2,bottom=2),
                        border_radius=15,
                        border=border.all(width=1,color='#1afefefe'),
                        content=Row(
                          controls=[
                            Icon(icons.SEARCH_OUTLINED,color='black12'),
                            TextField(
                              bgcolor=None,
                              border=InputBorder.NONE,
                              color='black',
                              hint_text='Search',
                              hint_style=TextStyle(color='black12',),
                            )
                          ]
                        )

                      )
                    ]
                  ),
                
                ]
              ),
              Container(
                clip_behavior=ClipBehavior.ANTI_ALIAS,
                height=250,
                width=640,
                # bgcolor='black',
                border_radius=35,
                margin=margin.only(bottom=20),
                content=Stack(
                  controls=[
                    Container(
                      height=250,
                      width=640,
                      content=Image(
                        src='assets/icons/model.jpg',
                        fit=ImageFit.COVER,
                      ),
                    ),
                    Container(
                      height=250,
                      width=640,
                      padding=padding.only(top=30,left=40,bottom=10,right=20),
                      content=Column(
                        spacing = 5,
                        controls=[
                          Text(
                            value='Newton Dark-Nights',
                            size=8,
                            font_family='SF Pro Regular'
                          ),
                          Container(
                            width=350,
                            content=Text(
                              value='Listen to trending songs all the time',
                              size=35,
                              font_family='SF Pro Semibold'
                            ),
                          ),
                          Container(
                            width=350,
                            content=Text(
                              value='With Taylor Swift\'s. You can get premium music for free anywhere at any time.',
                              size=12,
                              font_family='SF Pro Regular'
                            ),
                          ),
                          Container(
                            alignment=alignment.center,
                            width=120,
                            height=50,
                            bgcolor='#660e283f',
                            border_radius=25,
                            content=Text(
                              value='Explore Now',
                              size=12,
                              font_family='SF Pro Regular'
                            ),
                            on_click=self.shrink
                          ),

                        ]
                      )
                    ),
                    
                  ]
                )
              ),
              Row(
                alignment='spaceBetween'  ,
                controls=[
                  Text(
                    value="Music Library",
                    font_family='SF Pro Semibold',
                    color='black',
                    size=25,
                  ),
                  Container(
                    on_click=self.restore,
                    content=Column(
                    horizontal_alignment='center',
                    spacing=0,
                    controls=[
                      Text(
                        value='See all',
                        color='#656ca2',
                        font_family='SF Pro Regular',
                        size=16,
                      ),
                      Container(
                        height=1,bgcolor='#656ca2',width=50
                      )]
                    )
                  ),


                ]
              ),

              Container(
                height=2
              ),
              Container(
                expand=True,
                content=self.music_library_column
              
              )
            ]
          )
        )
      )
                
    ]
  ) 

  def artist_name(self):
    return Text(
      value='-',
      size=18,
      color='white',
      font_family='SF Pro Semibold'
    )
  def song_title(self):
    return Text(
      value='-',
      size=12,
      color='#dbdef6',
      font_family='SF Pro Regular',
    )

  def play_song(self,e: TapEvent):
    self.audio1.seek(self.audio_progress.padding.right)
    self.audio1.update()    
    if e.control.padding == 2:
      e.control.padding = 0
      e.control.update()
      self.audio1.resume()
    else:
      self.audio1.pause()  
      e.control.padding = 2
      e.control.update()
  def cover_art(self):
    return Image(
      src='assets/cover_arts/africaq.jpg',
      fit=ImageFit.COVER
    )

  def audio_player_details(self):
    return Container(
      padding=padding.only(top=20),
      height=480,
      width=310,
      bgcolor=pc,
      border_radius=35,
      margin=margin.only(bottom=55),
      content=Column(
        horizontal_alignment='center',
        controls=[
          Container(
            height=250,
            width=250,
            border_radius=20,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            content=self.cover_art,
          ),
          Container(
            height=100,
            width=290,
            content=Column(
              spacing=0,
              alignment='center',
              horizontal_alignment='center',
              controls=[
                self.artist_name,
                self.song_title,
              ]
            )
          ),

          Container(
            width=270,
            height=80,
            content=Row(
              alignment='spaceBetween',
              controls=[
                Container(
                  content=Image(
                          src='assets/icons/repeat.png',
                          color='white',
                          height=20,
                  )
                ),
                Container(
                  content=Row(
                    controls=[
                      Container(
                        content=Icon(
                          icons.SKIP_PREVIOUS,
                        )
                      ),
                      Container(
                        padding = 2,
                        on_click=self.play_song,
                        height=55,
                        width=55,
                        border_radius=30,
                        bgcolor='white',
                        content=Image(
                          src='assets/icons/play.png'
                        )
                      ),
                      Container(
                        content=Icon(
                          icons.SKIP_NEXT,
                        )
                      ),
                    ]
                  )
                ),
                Container(
                  height=20,
                  content=Image(
                    src='assets/icons/shuffle.png',
                    color='white'
                  )
                ),
              ]
            )
          )
        ]
      )
    )
  
  def click_seek(self,e: TapEvent):
    k = self.audio1.get_duration()/180
    e.control.padding.right = 180 - e.local_x
    self.audio1.seek(round(k*( e.local_x)))
    e.control.update()

  def audio_progress(self):
    return Container(
      on_click=self.click_seek,
      width=160,
      height=5,
      bgcolor='white12',
      border_radius=10,
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      padding=padding.only(right=160),
      content=Container(
        expand=True,
        bgcolor='white'
      ),
    )  

  def progress(self,e):
      # p = None
      # try:
      #   p = 160-round((cp / ad)*160,2)
      # except:
      #   p = 160  
      cp = self.audio1.get_current_position()
      ad = self.audio1.get_duration()
      self.audio_cur_pos.value = str(self.miliseconds_to_time(cp))
      self.audio_progress.padding.right = 160-round((cp / ad)*160,2)
      self.audio_cur_pos.update()
      self.audio_progress.update()
    
  def miliseconds_to_time(self,ms):
    if ms < 3600000:
        minutes, remainder = divmod(ms, 60000)
        seconds, _ = divmod(remainder, 1000)
        return '{:02}:{:02}'.format(int(minutes), int(seconds))
    else:
        hours, remainder = divmod(ms, 3600000)
        minutes, remainder = divmod(remainder, 60000)
        seconds, _ = divmod(remainder, 1000)
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

  # def seconds_to_time(self,s):
  #   if s < 3600000:
  #       minutes, remainder = divmod(ms, 60000)
  #       seconds, _ = divmod(remainder, 1000)
  #       return '{:02}:{:02}'.format(int(minutes), int(seconds))
  #   else:
  #       hours, remainder = divmod(ms, 3600000)
  #       minutes, remainder = divmod(remainder, 60000)
  #       seconds, _ = divmod(remainder, 1000)
  #       return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        
  def song_loaded(self,e):
    details = asyncio.run(self.song_details(self.audio_url))
 
    if details[2] == 'Unknown':
      details[2] = 'default.jpg'
    self.cover_art.src = 'assets/cover_arts/'+details[2]
    self.cover_art.update()

    self.song_title.value = details[0]
    self.song_title.update()

    self.artist_name.value = details[1]
    self.artist_name.update()
    
    dur = self.audio1.get_duration()
    self.audio_dur.value = str(self.miliseconds_to_time(dur))
    self.audio_dur.update()

  def load_songs_onstart(self,):
    # with open('data.json','r+') as file:
    #   file_data = json.load(file)
    #   songs = file_data["file_details"]
    # for song in songs:
    #   det = file_data["file_details"][song]
    #   print(det)
    pass  


      # self.music_library_column.controls.append(
      #   self.song_obj(
      #     artist='',
      #     cover_art='',
      #     title='',
      #     length='',
      #     streams='',
      #     like='f',
      #     num=''
      #   )
      #   )
      # self.music_library_column.update()


  def audio1(self):
    return Audio(
        src=self.audio_url,
        autoplay=False,
        volume=1,
        balance=0,
        on_position_changed=self.progress,
        on_loaded= self.song_loaded
        # on_duration_changed=lambda e: print("Duration changed:", e.data),
        # on_state_changed=lambda e: print("State changed:", e.data),
        # on_seek_complete=lambda _: print("Seek complete"),
    )  
  

  def audio_cur_pos(self):
    return Text(
      value='0:00',
      color='white',
      font_family='SF Pro Regular',
      size=10,
    )


  def audio_dur(self):
    return Text(
      value='0:00',
      color='white',
      font_family='SF Pro Regular',
      size=10,
    )


  def clicked(self,e: TapEvent):
    k = self.audio1.get_duration()/160
    e.control.padding.right = 160 - e.local_x
    self.audio1.seek(round(k*( e.local_x)))
    e.control.update()

    
  def load(self,e: DragUpdateEvent):
      # print(e.data)
      e.control.content.padding.right = max(0, e.control.content.padding.right - e.delta_x)
      if e.control.content.padding.right <= 0:
        e.control.content.padding.right = 0
      if e.control.content.padding.right >= 160:
        e.control.content.padding.right = 160  
      e.control.content.update()
  
  def audio_playtime_and_indicator(self):
    return Container(
      padding=padding.only(top=20,left=10,right=10),
      left=20,
      bottom=10,
      height=70,
      width=265,
      bgcolor=ac,
      border_radius=25,
      content=Row(
        alignment='spaceBetween',
        controls=[
          self.audio_cur_pos,

    # audio loading indicator...
          GestureDetector(
            mouse_cursor=MouseCursor.MOVE,
            content=self.audio_progress,
            on_vertical_drag_update=self.load,
            # on_scroll=load
          ),
          self.audio_dur,
        ]
      )

    )
  
  def sidebar_content_handler(self,):
    return Column(
                      # alignment='spaceBetween',
                      horizontal_alignment='center',
                      spacing=30,
                      controls=[
                      ]
                    )     
  
  def sidebar_btns_loader(self):
      self.sidebar_content_handler.controls.append(self.sidebar_button('home_outlined','home'))
      self.sidebar_content_handler.controls.append(self.sidebar_button('music_note_outlined','music'))
      self.sidebar_content_handler.controls.append(self.sidebar_button('folder_outlined','files'))

  def sidebar_btn_hover(self,e):
    if e.data == 'true':
      e.control.bgcolor = 'white12'
      e.control.content.color = 'white'
      e.control.content.src = e.control.content.src.replace('outlined','filled')
    else:
      e.control.bgcolor = None
      e.control.content.color = sbic
      e.control.content.src = e.control.content.src.replace('filled','outlined')
    e.control.update()  
      
  def sidebar_btn_click(self,e: TapEvent):
    if e.control.data == 'files':
      self.pick_files_dialog.pick_files(
        allow_multiple=True,
        dialog_title='Select songs',
      file_type=FilePickerFileType.AUDIO
    )
    
    




  def sidebar_button(self,icon:str,data):
    return Container(
      data=data,
      border_radius=30,
      height=40,
      width=40,
      padding=10,
      on_hover=self.sidebar_btn_hover,
      on_click=self.sidebar_btn_click,
      content=Image(src='assets/icons/'+icon+'.png',color=sbic)
    )
            
    
  def audio_player(self):
    return Container(
      height=580,
      content=Row(
        controls=[
          Stack(
            controls=[
              self.audio_playtime_and_indicator,

              self.audio_player_details,
            ]
          )
        ]
      )
    )
  async def save_file_details(self,key,new_data):
    with open('data.json','r+') as file:
      file_data = json.load(file)
      file_data["file_details"].append(new_data)
      # file_data["file_details"][key]=new_data
      file.seek(0)
      json.dump(file_data, file, indent = 4)

  async def song_de(self,f):
    try:
      aud = MP3(f)
      return aud.info.length
    except:
      return 'Unknown'  

  def load_songs(self,e: FilePickerResultEvent):
    if e.files:
      for file in e.files:
        fn = file.name
        d = asyncio.run(self.song_details1(file.path))
        a = d[0]
        t = d[1]
        c = d[2]
        length = asyncio.run(self.song_de(file.path))
        l = self.miliseconds_to_time(int(length)*1000)
        
        with open('index.txt','r')as f:
          i = int(f.readline())+1
        if i < 10:
          i = '0'+(str(i))
  
        print(a)
        print(t)
        print(c)
        
        y={
          "path":file.path,
          "liked":False,
          "length":l,
          "num":i,
          "nol":0,
        }
        
        asyncio.run(self.save_file_details(fn,y))
        
        with open('index.txt','r') as f:
          k = int(f.readline())+1 
        with open('index.txt','w') as f:
          f.write(str(k))  

        if c == "Unknown":
          c = 'default.jpg'
        self.music_library_column.controls.append(
          self.song_obj(
            artist=a,
            title=t,
            cover_art=c,
            length=l,
            streams='12032',
            like='false',
            num=i
          )
        )
        self.music_library_column.update()



  def playlist_obj(self):
    return Container(
      padding=15,
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      height=170,
      width=170,
      bgcolor='#011243',
      image_src='assets/cover_arts/africaq.jpg',
      image_fit=ImageFit.COVER,
      image_opacity=0.9,
      border_radius=35,
      content=Column(
        horizontal_alignment='center',
        alignment='spaceBetween',
        controls=[
          
          Container(
            width=150,
            height=30,
            content=Row(
              alignment='end',
              controls=[
                Container(
                  # width=180,
                  padding=padding.only(right=15),
                  content=Row(
                    spacing=2,
                    controls=[
                      Container(height=3.5,width=3.5,bgcolor='white',border_radius=5),
                      Container(height=3.5,width=3.5,bgcolor='white',border_radius=5),
                      Container(height=3.5,width=3.5,bgcolor='white',border_radius=5),
                    ]
                  )
                ),
              ]

            )
          ),
          
          Container(
            width=150,
            height=55,
            gradient=LinearGradient(
              colors=[
                '#cc392890',
                '#992c2887',
                '#b3252985',
                '#cc392890',
              ]
            ),
            border_radius=15,
            padding=5,
            content=Row(
              alignment='spaceBetween',
              controls=[
                Container(
                  clip_behavior=ClipBehavior.ANTI_ALIAS,
                  padding=padding.only(right=5),
                  width=85,
                  content=Row(
                    spacing=4,
                    controls=[
                      Icon(icons.MUSIC_NOTE_OUTLINED,size=10),
                      Text(
                        value='The dark side',
                        size=10,

                      )
                    ]
                  
                  ),
                ),
                Container(
                  height=35,
                  width=35,
                  bgcolor='white',
                  border_radius=40,
                  content=Icon(icons.PLAY_ARROW,color='black'),
                )
              ]
            )
          ),

        ]
      )
    
    )   
  
  def playlists_content(self):
    return Row(
      spacing = 20,
      scroll='auto',
      width=370,
      controls=[
        self.playlist_obj,
        self.playlist_obj,
      ]
    )




  def base_layout(self):
    return Row(
      alignment='end',
      controls=[
        Container(
          width=w,
          height=h,
          bgcolor=sb,
          border_radius=35,
          animate=animation.Animation(1000,AnimationCurve.BOUNCE_OUT),
          animate_scale=animation.Animation(400, curve='decelerate'),
          animate_opacity=animation.Animation(1200, curve='decelerate'),
          content=Stack(
          controls=[
            Container(
              width=80,
              height=h,
              padding=padding.only(top=50,bottom=50),
              alignment=alignment.center,
              content=Column(
                alignment='spaceBetween',
                horizontal_alignment='center',
                controls=[
                  Container(
                    height=40,
                    width=40,
                    border_radius=20,
                    bgcolor=ic,
                    content=Container(
                      content=Image(
                        src='assets/icons/disk.png',
                        color='white'
                      )
                    )
                  ),
                  Container(
                    self.sidebar_content_handler,
                  ),
                  Container(
                    content=Icon(icons.SETTINGS_OUTLINED,color='white12')
                  )

                ]
              )
            ),
            
            Container(
              padding = padding.only(left=30),
              expand = True,
              left=80,
              border_radius=25,
              bgcolor=mb,
              width=1100,
              height=852,
              content=Stack(
                controls=[
                  Column(
                    controls=[
                      Container(
                        height=30,
                        content=WindowDragArea(content=Container())),
                      Container(
                        content=Row(
                          controls=[
                            Text(
                              'Playlists',
                              size=25,
                              font_family='SF Pro Semibold'
                            )
                          ]
                        )
                      ),
                      Container(
                        height=180  ,
                        content=self.playlists_row

                      ),
                      self.audio_player
                    
                    ]

                  ),
                  
                
                ]
              )
            
            ),
          ]
        )
        )
      ]
    ) 


  
  async def song_details(self,filename):
    try:
      audio = MP3(f"assets/audio/{filename}")
      artist = audio.get('TPE1')
      title = audio.get('TIT2')
      cover = audio.tags.get("APIC:").data
      if cover:
        with open(f"assets/cover_arts/{filename.split('.')[0]}.jpg", "wb") as cover_art:
          cover_art.write(cover)
      k = [artist,title,f"{filename.split('.')[0]}.jpg"]
      details = []
      for n in k:
        if n is None:
          n = 'Unknown'
        details.append(n)  
      return details  

    except:
      return ['Artist unknown','Title unknown','Unknown']  
  
  async def song_details1(self,filename):
    try:

      audio = MP3(f"{filename}")

      artist = audio.get('TPE1')
      title = audio.get('TIT2')
      cover = audio.tags.get("APIC:")
      
      f= os.path.basename(filename).split('.')[0]+'.jpg'
      if cover:
        cov = cover.data
        with open(f"assets/cover_arts/{f}", "wb") as cover_art:
          cover_art.write(cov)
      else:
        f = None 
      k = [artist,title,f]
      details = []
      for n in k:
        if n is None:
          n = 'Unknown'
        details.append(n)  
      return details  

    except:
      return ['Artist unknown','Title unknown','Unknown']  
  
  async def add_song_to_library(self,):
    self.music_library_column.controls.append(Container())
    self.music_library_column.update()



t = App
app(target=t,assets_dir='assets')


  