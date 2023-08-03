import streamlit as st
import os

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import rc

import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title = 'KBO NC dinos Dashboard',
    page_icon = '⚾️',
    layout = 'wide',
    initial_sidebar_state = 'collapsed',
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 데이터 로드
def get_df():
    
    team_df = pd.read_csv(os.path.join(os.getcwd(), 'data/team_rank_table_2008_2018.csv'))
    bat_df = pd.read_csv(os.path.join(os.getcwd(), 'data/nan_processed_batter_df.csv'))
    bat_image = pd.read_csv(os.path.join(os.getcwd(), 'data/nc_player_img.csv'))
    
    return team_df, bat_df, bat_image

team_colors = {
    'LG': 'rgba(195, 4, 66, 0.5)',  # '#B82E2E',
    '한화': 'rgba(255, 102, 0, 0.5)',  # '#FF7F0E',
    'NC': 'rgb(49, 82, 136)',  # '#3366CC',
    '삼성': 'rgba(7, 76, 161, 0.5)',  # 'blue',
    '롯데': 'rgba(4, 30, 66, 0.5)',  # 'black',
    'KT': 'rgba(0, 0, 0, 0.5)',  # 'darkgray',
    '키움': 'rgba(87, 5, 20, 0.5)',  #'#D62728',
    'SK': 'rgba(206, 14, 45, 0.5)',  # 'red',
    'KIA': 'rgba(235, 0, 41, 0.5)',  # 'rgb(237, 28, 36)',
    '두산': 'rgba(19, 18, 48, 0.5)'  # 'purple'
}

koreanize_dict = {'타율': 'avg',
                  '장타율': 'SLG',
                  '출루율': 'OBP',
                  'OPS': 'OPS',
                  '경기당 득점': 'R/G',
                  '경기당 타점': 'RBI/G',
                  '경기당 안타': 'H/G',
                  '경기당 홈런': 'HR/G',
                  '경기당 루타수': 'TB/G',
                  '경기당 도루성공': 'SB/G',
                  '경기당 도루실패': 'CS/G',
                  '경기당 볼넷': 'BB/G',
                  '경기당 삼진': 'SO/G',
                  '경기당 병살타': 'GDP/G'
                 }

team_df, bat_df, bat_image = get_df()

# 선수 프로필 이미지 크롤링
@st.cache_data
def scrap_player_image(player_name):
    st.write(player_name)
    
    baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
    
    url = baseUrl+'야구선수'+player_name
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    
    img = soup.select_one('.thumb > img')['src']
    
    if img=='https://search.pstatic.net/sunny?src=https%3A%2F%2Fwww.ncdinos.com%2Fassets%2Fimages%2Ffavicon.ico&type=f30_30_png_expire24':
        url = baseUrl+player_name
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
    
        img = soup.select_one('a.thumb > img')['src']

    # player_names = list(bat_df[bat_df['team']=='NC']['batter_name'].unique())
    # player_image_dict = dict()
    
    
    # for player_name in player_names:
    #     baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
    #     url = baseUrl+'야구선수'+player_name
    #     html = requests.get(url).text
    #     soup = BeautifulSoup(html, 'html.parser')
    
    #     img = soup.select_one('.thumb > img')['src']
    
    #     if img=='https://search.pstatic.net/sunny?src=https%3A%2F%2Fwww.ncdinos.com%2Fassets%2Fimages%2Ffavicon.ico&type=f30_30_png_expire24':
    #         url = baseUrl+player_name
    #         html = requests.get(url).text
    #         soup = BeautifulSoup(html, 'html.parser')
    
    #         img = soup.select_one('a.thumb > img')['src']
    
    #     player_image_dict[player_name] = img

    return img



# 사이드바에서 사용자가 조회할 연도 선택
with st.sidebar:
    st.subheader(':blue[NC] dinos Dashboard')
    st.divider()
    st.markdown('**조회하고 싶은 연도를 선택하세요**')
    st.selectbox(
        '**조회하고 싶은 연도를 선택하세요**',
        team_df['연도'].unique(),
        key = 'year'
    )
    st.divider()
    st.selectbox(
        '**조회하고 싶은 지표를 선택하세요**',
        ['avg', 'R', 'RBI', 'H', 'HR', 'TB', 'SB', 'CS', 'BB', 'HBP', 'SO'],
        key = 'stat'
    )
    st.divider()

    start_color, end_color = st.select_slider(
        'Select a range of color wavelength',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('You selected wavelengths between', start_color, 'and', end_color)
    # st.selectbox(
    #     '**조회하고 싶은 선수를 선택하세요**',
    #     bat_df.loc[bat_df['team'] == 'NC', 'batter_name'].unique(),
    #     key = 'player'
    # )

    

col1, col2, col3 = st.columns((3.5, 5.5, 1))

# 대시보드 타이틀
with col1:
    st.image("https://www.ncdinos.com/assets/images/sub/emblem01.png"
            ,width = 150)
    st.write('')
with col2:
    st.header(':blue[KBO] NC dinos Dashboard')  # st.header('KBO NC dinos Dashboard')
with col3:
    st.write('')
    st.image("https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/KBOHome/resources/images/common/h1_logo.png"
            ,width = 170)
st.divider()


    
col1, col2 = st.columns(2, gap = 'large')

# 팀 순위 테이블
with col1:
    
    # st.subheader(f'{st.session_state.year}년도 KBO 구단 순위')
    # st.caption('사이드바에서 조회하고 싶은 연도를 선택해주세요.')
    # sub_col1,  _ = st.columns((1.5, 8.5))
    # with sub_col1:
    #     # st.markdown('**KBO 구단 순위**')
    #     year = st.selectbox('**KBO 구단 순위**',team_df['연도'].unique())  # , label_visibility = 'collapsed'
    # with sub_col2:
    #     st.markdown(f'{st.session_state.year}년도 KBO 구단 순위')
    # st.write('')
    # st.write('')

    sub_col1, _, sub_col2, _ = st.columns((5, 1.2, 1.5, 2.3))

    with sub_col2:
        year = st.selectbox('**2008-2018년 구단별 평균 타격 지표**', team_df['연도'].unique(), label_visibility = 'collapsed')
    with sub_col1:
        st.subheader('**KBO 구단 순위**')
    
    team_tmp = team_df.copy()
    st.dataframe(team_tmp.loc[team_tmp['연도'] == year, '순위':'방문'],
                 hide_index = True,
                 # width = 725,
                 height = 420,
                 use_container_width = True
                )


# 연도별 팀 순위 라인차트
with col2:
    # st.subheader("연도별 KBO 구단 성적")
    selected_team = st.multiselect(label = "**구단을 선택하세요**",
                                   options = team_df['팀명'].unique(),
                                   default = 'NC'
                                   # label_visibility = 'collapsed',
                                   # key = 'team_line',
                                   )

    team_tmp = team_df.copy()
    
    # fig = px.line(team_tmp[team_tmp['팀명'].isin(st.session_state.team_line)], x = '연도', y = '순위', color = '팀명'
    #              ,hover_data = ['승', '무', '패', '팀명', '승률']
    #              ,color_discrete_map = team_colors)
    
    # fig.update_traces(hovertemplate = "<b>연도: %{x}</b><br><b>순위: %{y}위</b><br><b>%{customdata[0]}승 %{customdata[1]}무 %{customdata[2]}패</b><br><b>승률: %{customdata[4]}</b>")
    # fig.update_layout(yaxis = dict(range=[10, 0], title = 'KBO 구단 연도별 순위'))

    fig = go.Figure()
    
    for team in team_tmp['팀명'].unique():
        team_data = team_tmp[team_tmp['팀명'] == team]
        
        if team in selected_team:
            fig.add_trace(go.Scatter(x = team_data['연도'], y = team_data['순위'], name = team,
                                     line = dict(color = team_colors[team]),
                                     marker = dict(size = 4),
                                     customdata = team_data.loc[:, ['승', '무', '패', '팀명', '승률']],
                                     hovertemplate = "<b>팀명: %{customdata[3]}</b><br><b>연도: %{x}</b><br><b>%{customdata[0]}승 %{customdata[1]}무 %{customdata[2]}패</b><br><b>승률: %{customdata[4]}</b>"))
        else:
            fig.add_trace(go.Scatter(x = team_data['연도'], y = team_data['순위'], name = team,
                                     line = dict(color = 'rgba(192, 192, 192, 0.5)'),
                                     marker = dict(size = 4),
                                     customdata = team_data.loc[:, ['승', '무', '패', '팀명', '승률']],
                                     hovertemplate = "<b>팀명: %{customdata[3]}</b><br><b>연도: %{x}</b><br><b>%{customdata[0]}승 %{customdata[1]}무 %{customdata[2]}패</b><br><b>승률: %{customdata[4]}</b>"))

    fig.update_layout(
        title = 'KBO 구단 연도별 순위',
        # xaxis_title='연도',
        yaxis_title='순위',
        yaxis = dict(range=[10.5, 0.5]),
        margin = dict(l = 0, r = 0, t = 50, b = 10),
        height = 400,
        width = 725
    )

    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)


    


# col1, col2, col3 = st.columns((5, 1, 4), gap = 'small')

col1, col2 = st.columns(2, gap = 'small')

temp_bat = bat_df.copy()
temp_team = team_df.copy()

with col1:
    bat_columns = ['year', 'team', 'avg', 'R', 'H', 'HR', 'TB', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP', 'OPS']
    
    # 팀과 연도로 그룹화된 데이터프레임 생성
    group_df = temp_bat.groupby(['team', 'year'])
    
    # 그룹화된 데이터프레임에 대해 지표들의 합계 계산
    agg_df = group_df.agg({
        'R': 'sum', 'H': 'sum', 'HR': 'sum', 'TB': 'sum', 'RBI': 'sum', 'SB': 'sum',
        'CS': 'sum', 'BB': 'sum', 'HBP': 'sum', 'SO': 'sum', 'GDP': 'sum',
        'avg': 'mean', 'SLG': 'mean', 'OBP': 'mean', 'OPS': 'mean'}).reset_index()
    
    agg_df = agg_df.merge(temp_team.loc[:, '연도':'승률'], left_on = ['year', 'team'], right_on = ['연도', '팀명']).drop(columns = ['연도', '팀명'])
    # 컬럼 재정렬
    agg_df = agg_df[['year', 'team', '경기', '승', '패', '무', '순위', '승률', 'avg', 'R', 'RBI', 'H', 'HR', 'TB', 'SB', 'CS', 'BB', 'SO', 'GDP', 'SLG', 'OBP', 'OPS']]
    
    def stats_by_g(df, stats):
        # 연도별 구단의 각 지표의 합을 경기 수로 나눔 => 경기 당 횟수
        col_names = [f'{stat}/G' for stat in stats]
        
        div_df = df.apply(lambda x: x[stats] / x['경기'], axis = 1)
        div_df.columns = col_names
        df = pd.concat([df, div_df], axis = 1).drop(columns = stats)
    
        return df
    
    agg_df = stats_by_g(agg_df, ['R', 'RBI', 'H', 'HR', 'TB', 'SB', 'CS', 'BB', 'SO', 'GDP'])
    
    agg_col = agg_df.loc[:, '순위':].columns
    agg_df = agg_df.groupby(['team'])[agg_col].mean().sort_values(by = '순위')
    
    def rank_scaling(df):
        # 1-10 범위 값을 갖는 rank를 0-1로 min-max 스케일링
        df['scaled_rank'] = 1 - ((df['순위'] - df['순위'].min()) / (df['순위'].max() - df['순위'].min()))
        return df
    
    agg_df = rank_scaling(agg_df)

    sub_col1, _, sub_col2, _ = st.columns((5, 1, 1.7, 2.3))

    with sub_col1:
        st.subheader('**2008-2018년 구단별 평균 타격 지표**')
    with sub_col2:
        stat = st.selectbox('**2008-2018년 구단별 평균 타격 지표**', koreanize_dict.keys(), label_visibility = 'collapsed')
        # stat = st.selectbox('**2008-2018년 구단별 평균 타격 지표**', agg_df.loc[:, 'avg':'GDP/G'].columns, label_visibility = 'collapsed')

    stat = koreanize_dict[stat]
        
    # 시각화
    min_xaxis = np.floor(agg_df[stat].min())
    max_xaxis = np.ceil(agg_df[stat].max())
    xtick = round((max_xaxis - min_xaxis)/5)
    
    if agg_df[stat].min() < 1:
        min_xaxis = np.floor(agg_df[stat].min() * 100) / 100
        max_xaxis = np.ceil(agg_df[stat].max() * 100) / 100
        xtick = round((max_xaxis - min_xaxis) / 5 * 100) / 100
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(x = agg_df.index, y = agg_df[stat], name=f'평균 {stat}',
                         marker = dict(color = [team_colors.get(team) for team in agg_df.index])))
    
    # hover에 해당 지표의 25% max 75%? => 전체 스탯에 대한 df를 "스탯이 선택되면 df를 생성하게 해야함"
    # 평균 순위, 승률, 우승년도, 선택된 스탯
    
    fig.update_layout(
        yaxis = dict(range=[min_xaxis, max_xaxis], dtick=xtick),
        margin = dict(t=20, l=0, r=0),
        # autosize = True
        width = 725,
        height = 500,
    )
    
    st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)

    
    # # 미정 -> 2008-2018년 구단별 평균 순위를 보여주고 타율 등 지표를 대비시켜 순위를 결정하는데 어떤 지표가 중요한지 탐색 가능하도록
    # # +) 응원하는 팀의 지표를 대략적으로 탐색 가능하도록
    # # 홈런 등 지표는 경기당 횟수로

    # st.subheader('2008-2018년 구단 평균 타격 지표')
    
    # bat_tmp = bat_df.copy()

    # bat_columns = ['year', 'team', 'avg', 'R', 'H', 'HR', 'TB', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP', 'OPS']
    # bat_tmp = bat_tmp[bat_columns]
    # bat_tmp = bat_tmp.rename(columns = {'year': '연도', 'team': '팀명'})

    # tb_df = team_df.loc[:, '연도':'승률'].merge(bat_tmp, on = ['연도', '팀명']).groupby(['연도', '팀명']).mean().reset_index()
    # avg_rank = tb_df.groupby('팀명').mean().reset_index().sort_values('순위')

    # team_order = avg_rank['팀명'].to_list()
    # tb_df['팀명'] = pd.Categorical(tb_df['팀명'], categories = team_order, ordered = True)
    # tb_df = tb_df.sort_values(by = '팀명')
    
    # fig = go.Figure()

    # fig.add_trace(go.Bar(x = tb_df.loc[tb_df['연도'] == st.session_state.year, '팀명'], y = tb_df.loc[tb_df['연도'] == st.session_state.year, st.session_state.stat],
    #                      name = f'평균 {st.session_state.stat}', yaxis='y2', marker = dict(color = [team_colors.get(team) for team in tb_df.loc[tb_df['연도'] == st.session_state.year, '팀명']])))  # 
    # fig.add_trace(go.Scatter(x = avg_rank['팀명'], y = avg_rank['순위'], name = '평균 순위', yaxis = 'y', marker_color = 'rgb(0, 32, 99)',
    #                          hovertemplate = '<b>구단: %{x}</b><br><b>평균 순위: %{y}위</b>',
    #                          hoverlabel = dict(font = dict(size = 12)),
    #                          ))
    
    # fig.update_layout(
    #     yaxis = dict(range = [12, 1], dtick = 1, showticklabels = False, showgrid = False),
    #     yaxis2 = dict(range = [0.15, 0.65], dtick = 0.1, overlaying = 'y', side = 'right'),
    #     width = 750,
    #     height = 600,
    #     legend = dict(x = 1.1, y = 0.9),
    #     margin = dict(t = 0, l = 0, r = 0),
    # )
    # # fig.update_xaxes(categoryorder = 'array', categoryarray = avg_rank['팀명'])
    # st.plotly_chart(fig, theme = 'streamlit')

with col2:
    # 포수 / 내야수 / 외야수
    df = bat_df.copy()
    df = df.rename(columns = {'팀명': 'team'})

    # st.subheader('구단 포지션별 OPS Boxplot')

    sub_col1, sub_col2 = st.columns((1.3, 8.7), gap = 'small')
    
    positions = ['내야수','외야수','포수']
    selected_positions, options = sub_col1.selectbox('포지션', positions), sub_col2.multiselect('팀을 선택하세요.', df['team'].unique(), df['team'].unique())

    
    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    
    select_team_df = df[df['team'].isin(options)]
    
    try:
        if selected_positions == '내야수':
            # Streamlit 앱 생성
            # st.title('팀별 내야수 Box Plot')
            # st.write('여기에 박스 플롯이 나타납니다.')
    
            in_df = select_team_df[select_team_df['position'].str.contains('내야수')==True] # 내야수
    
            # 박스 플롯 그리기
            fig1, ax1 = plt.subplots()
            fig1 = px.box(in_df, x='team', y='OPS')
            # in_df.boxplot(column='OPS', by='team', ax=ax1)
            st.plotly_chart(fig1)
    
    
        elif selected_positions=='외야수':
            # st.title('팀별 외야수 Box Plot')
            # st.write('여기에 박스 플롯이 나타납니다.')
    
            out_df = select_team_df[select_team_df['position'].str.contains('외야수')==True] # 외야수
    
            # 박스 플롯 그리기
            fig2, ax2 = plt.subplots()
            fig2 = px.box(out_df, x='team', y='OPS')
            # out_df.boxplot(column='OPS', by='team', ax=ax2)
            st.plotly_chart(fig2)
    
        elif selected_positions=='포수':
            # st.title('팀별 포수 Box Plot')
            # st.write('여기에 박스 플롯이 나타납니다.')
    
            home_df = select_team_df[select_team_df['position'].str.contains('포수')==True] # 포수
    
            # 박스 플롯 그리기
            fig3, ax3 = plt.subplots()
            fig3 = px.box(home_df, x='team', y='OPS')
            # home_df.boxplot(column='OPS', by='team', ax=ax3)
            st.plotly_chart(fig3)
    
    except:
        fig4, ax4 = plt.subplots()
        st.plotly_chart(fig4)


    
    # # 팀별 OPS 박스플롯

    # df = bat_df.copy()
    # df = df.rename(columns = {'팀명': 'team'})

    # # st.subheader('구단 포지션별 OPS Boxplot')

    # sub_col1, sub_col2 = st.columns((1.3, 8.7), gap = 'small')
    
    # positions = ['내야수','외야수','포수']
    
    # selected_positions, options = sub_col1.selectbox('포지션', positions), sub_col2.multiselect('팀을 선택하세요.', df['team'].unique(), df['team'].unique())
    # # st.write(temp)
    
    # # selected_positions = st.selectbox('포지션을 선택하세요', positions)
    # # options = st.multiselect(
    # #     '팀을 선택하세요.',
    # #     df['team'].unique(),
    # #     df['team'].unique())
    
    # rc('font', family='AppleGothic')
    # plt.rcParams['axes.unicode_minus'] = False
    
    # select_team_df = df[df['team'].isin(options)]
    
    # try:
    #     if selected_positions == '내야수':
    #         # Streamlit 앱 생성
    #         # st.title('팀별 내야수 Box Plot')
    #         # st.write('여기에 박스 플롯이 나타납니다.')
    
    #         in_df = select_team_df[select_team_df['position'].str.contains('내야수')==True] # 내야수
    
    #         # 박스 플롯 그리기
    #         fig1, ax1 = plt.subplots()
    #         in_df.boxplot(column='OPS', by='team', ax=ax1)
    #         st.pyplot(fig1)
    
    #     elif selected_positions=='외야수':
    #         # st.title('팀별 외야수 Box Plot')
    #         # st.write('여기에 박스 플롯이 나타납니다.')
    
    #         out_df = select_team_df[select_team_df['position'].str.contains('외야수')==True] # 외야수
    
    #         # 박스 플롯 그리기
    #         fig2, ax2 = plt.subplots()
    #         out_df.boxplot(column='OPS', by='team', ax=ax2)
    #         st.pyplot(fig2)
    
    #     elif selected_positions=='포수':
    #         # st.title('팀별 포수 Box Plot')
    #         # st.write('여기에 박스 플롯이 나타납니다.')
    
    #         home_df = select_team_df[select_team_df['position'].str.contains('포수')==True] # 포수
    
    #         # 박스 플롯 그리기
    #         fig3, ax3 = plt.subplots()
    #         home_df.boxplot(column='OPS', by='team', ax=ax3)
    #         st.pyplot(fig3)
    
    # except:
    #     fig4, ax4 = plt.subplots()
    #     st.pyplot(fig4)




st.divider()

col1, col2, col3 = st.columns((2, 4, 4), gap = 'small')
nc_bat = bat_df.loc[bat_df['team'] == 'NC']

# 선수 프로필 이미지
with col1:
    sub_col1, sub_col2, _ = st.columns((3, 3.5, 3.5))
    with sub_col1:
        p_year = st.selectbox('**연도**', nc_bat.sort_values('year', ascending = False)['year'].unique())
    with sub_col2:
        nc_player = st.selectbox('**NC 선수 선택**', nc_bat.loc[nc_bat['year'] == p_year, 'batter_name'].unique())
        # st.selectbox(
        #     '**NC 선수 선택**',
        #     nc_bat.loc[nc_bat['year'] == p_year, 'batter_name'].unique(),
        #     key = 'player',
        #     # label_visibility = 'collapsed',
        # )
    mercenary = ['스크럭스', '테임즈']

    nc_bat = nc_bat.loc[nc_bat['year'] == p_year]
    
    sub_col1, sub_col2 = st.columns((6.3, 3.7))
    with sub_col1:
        if nc_player in mercenary:
            st.write('')
            st.write('')
            st.image('https://www.ncdinos.com/assets/images/sub/mascots01.png', width = 200)
        else:
            st.image(bat_image.loc[bat_image['Player Name'] == nc_player, 'Image'].values[0], use_column_width = True)  # width = 200
    with sub_col2:

        def get_player_detail(column):
            value = nc_bat.loc[nc_bat['batter_name'] == nc_player, column].values[0]
            if value is np.nan:
                return '데이터가 없습니다'
            return value

        nc_p_position = get_player_detail('position')
        nc_p_g = get_player_detail('G')
        nc_p_r = get_player_detail('R')
        nc_p_rbi = get_player_detail('RBI')
        nc_p_hw = get_player_detail('height/weight')
        
        # nc_p_position = nc_bat.loc[nc_bat['batter_name'] == nc_player, 'position'].values[0]
        # nc_p_g = nc_bat.loc[nc_bat['batter_name'] == nc_player, 'G'].values[0]
        # nc_p_r = nc_bat.loc[nc_bat['batter_name'] == nc_player, 'R'].values[0]
        # nc_p_rbi = nc_bat.loc[nc_bat['batter_name'] == nc_player, 'RBI'].values[0]
        
        st.write('**세부정보**')
        st.write(nc_player)
        st.write(nc_p_hw)
        st.write(nc_p_position)
        # 출전 경기 수, 득점, 타점
        st.write(f'출전 경기 수:{nc_p_g}')
        st.write(f'득점:{nc_p_r} / 타점:{nc_p_rbi}')
    # st.image(scrap_player_image(st.session_state.player))
    # st.image(player_image_df.loc[player_image_df['Player Name'] == st.session_state.player, 'Image'].values[0])

    # st.image(scrap_player_image(st.session_state.player), width = 200)
    
    # st.image("https://file.sportsseoul.com/news/legacy/2016/08/29/news/20160829154410_51_1459042906_27104120_profile.jpg"
    #         ,width = 200)

# NC선수의 팀 내 홈런 기여 비율
with col2:
    container = st.container()
    nc_colors = [
        'rgba(49, 82, 136, 0.8)',
        'rgba(198, 159, 120, 0.8)'
    ]

    nc_bat['BB/K'] = np.where(nc_bat['SO'] == 0, nc_bat['BB'], round(nc_bat['BB'] / nc_bat['SO'], 3))
    
    nc_bat = nc_bat.rename(columns = {'BB': '볼넷', 'SO': '삼진'})

    # st.subheader('삼진 대비 볼넷 비율')
    player_bb_so = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player)][['볼넷', '삼진']]

    if player_bb_so.sum(axis = 1).values[0] != 0:
        bbk = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player), 'BB/K'].values[0]
        
        player_bb_so = player_bb_so.T.reset_index()
        player_bb_so.columns = ['Category', 'Count']
        player_bb_so['Category'] = pd.Categorical(player_bb_so['Category'], categories = ['볼넷', '삼진'], ordered = True)
        
        fig = go.Figure()
        fig.add_trace(go.Pie(labels = player_bb_so['Category'], values = player_bb_so['Count'], hole=0.5,
                             marker = dict(colors = nc_colors),
                             sort = False,
                             hovertemplate = f'<b>선수명: {nc_player} </b><br><b>연도: {str(p_year)}</b></br>'+'<b>%{label}: %{value}</b>'))
        # fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
        fig.update_layout(legend = dict(font = dict(size = 14)),
                          margin = dict(l = 0, r = 100),
                          title = '평균 삼진 대비 볼넷 비율',
                          title_font_size = 20)
        fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))

        container.plotly_chart(fig, theme = 'streamlit', use_container_width = True)
    else:  # 해당 연도에 데이터가 모두 0
        bbk = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player), 'BB/K'].values[0]
    
        empty = pd.DataFrame({'Category': ['볼넷', '삼진'], 'Count': [1, 1]})
        
        fig = go.Figure()
        fig.add_trace(go.Pie(labels = empty['Category'], values = empty['Count'], hole=0.5,
                             marker = dict(colors = nc_colors),
                             sort = False,
                             hovertemplate = f'<b>선수명: {nc_player} </b><br><b>연도: {str(p_year)}</b></br>'+'<b>%{label}: 0</b>'))
        fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
                          margin = dict(l = 0, r = 100),
                          title = '평균 삼진 대비 볼넷 비율',
                          title_font_size = 20)
        fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))

        container.plotly_chart(fig, theme = 'streamlit', use_container_width = True)
    
with col3:

    nc_colors = {
        '볼넷': 'rgba(49, 82, 136, 0.8)',
        '삼진': 'rgba(198, 159, 120, 0.8)'
    }

    nc_bat = bat_df[bat_df['team'] == 'NC']
    nc_bat['BB/K'] = np.where(nc_bat['SO'] == 0, nc_bat['BB'], round(nc_bat['BB'] / nc_bat['SO'], 3))
    
    nc_bat = nc_bat.rename(columns = {'BB': '볼넷', 'SO': '삼진'})

    # st.subheader('삼진 대비 볼넷 비율')
    player_bb_so = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player)][['볼넷', '삼진']]

    if player_bb_so.sum(axis = 1).values[0] != 0:
        bbk = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player), 'BB/K'].values[0]
        
        player_bb_so = player_bb_so.T.reset_index()
        player_bb_so.columns = ['Category', 'Count']
        player_bb_so['Category'] = pd.Categorical(player_bb_so['Category'], categories = ['볼넷', '삼진'], ordered = True)
        
        fig = go.Figure()
        fig.add_trace(go.Pie(labels = player_bb_so['Category'], values = player_bb_so['Count'], hole=0.5,
                             marker = dict(colors = [nc_colors[label] for label in player_bb_so['Category']]),
                             sort = False,
                             hovertemplate = f'<b>선수명: {nc_player} </b><br><b>연도: {str(p_year)}</b></br>'+'<b>%{label}: %{value}</b>'))
        fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
                          margin = dict(l = 0, r = 100),
                          title = '평균 삼진 대비 볼넷 비율',
                          title_font_size = 20)
        fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))

        st.plotly_chart(fig, theme = 'streamlit')
        
    else:  # 해당 연도에 데이터가 모두 0
        bbk = nc_bat.loc[(nc_bat['year'] == p_year) & (nc_bat['batter_name'] == nc_player), 'BB/K'].values[0]
    
        empty = pd.DataFrame({'Category': ['볼넷', '삼진'], 'Count': [1, 1]})
        
        fig = go.Figure()
        fig.add_trace(go.Pie(labels = empty['Category'], values = empty['Count'], hole=0.5,
                             marker = dict(colors = [nc_colors[label] for label in empty['Category']]),
                             sort = False,
                             hovertemplate = f'<b>선수명: {nc_player} </b><br><b>연도: {str(p_year)}</b></br>'+'<b>%{label}: 0</b>'))
        fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
                          margin = dict(l = 0, r = 100),
                          title = '평균 삼진 대비 볼넷 비율',
                          title_font_size = 20)
        fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))

        st.plotly_chart(fig, theme = 'streamlit')
    
    # try:
    #     if player_bb_so.sum(axis = 1).values[0] != 0:

    #         bbk = nc_bat.loc[(nc_bat['year'] == st.session_state.year) & (nc_bat['batter_name'] == st.session_state.player), 'BB/K'].values[0]
            
    #         player_bb_so = player_bb_so.T.reset_index()
    #         player_bb_so.columns = ['Category', 'Count']
    #         player_bb_so['Category'] = pd.Categorical(player_bb_so['Category'], categories = ['볼넷', '삼진'], ordered = True)
            
    #         fig = go.Figure()
    #         fig.add_trace(go.Pie(labels = player_bb_so['Category'], values = player_bb_so['Count'], hole=0.5,
    #                              marker = dict(colors = [nc_colors[label] for label in player_bb_so['Category']]),
    #                              sort = False,
    #                              hovertemplate = f'<b>선수명: {st.session_state.player} </b><br><b>연도: {str(st.session_state.year)}</b></br>'+'<b>%{label}: %{value}</b>'))
    #         fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
    #                           margin = dict(l = 0, r = 100),
    #                           title = '평균 삼진 대비 볼넷 비율',
    #                           title_font_size = 20)
    #         fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))
    
    #         st.plotly_chart(fig, theme = 'streamlit')
    #     else:  # 해당 연도에 데이터가 모두 0
    #         bbk = nc_bat.loc[(nc_bat['year'] == st.session_state.year) & (nc_bat['batter_name'] == st.session_state.player), 'BB/K'].values[0]
        
    #         empty = pd.DataFrame({'Category': ['볼넷', '삼진'], 'Count': [1, 1]})
            
    #         fig = go.Figure()
    #         fig.add_trace(go.Pie(labels = empty['Category'], values = empty['Count'], hole=0.5,
    #                              marker = dict(colors = [nc_colors[label] for label in empty['Category']]),
    #                              sort = False,
    #                              hovertemplate = f'<b>선수명: {st.session_state.player} </b><br><b>연도: {str(st.session_state.year)}</b></br>'+'<b>%{label}: 0</b>'))
    #         fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
    #                           margin = dict(l = 0, r = 100),
    #                           title = '평균 삼진 대비 볼넷 비율',
    #                           title_font_size = 20)
    #         fig.add_annotation(text = f'BB/K: {bbk}', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))
    
    #         st.plotly_chart(fig, theme = 'streamlit')
    # except:  # 해당 연도에 선수가 NC에 없음
    #     empty = pd.DataFrame({'Category': ['선수가 팀에 없습니다'], 'Count': [1]})
    #     fig = go.Figure()
    #     fig.add_trace(go.Pie(labels = empty['Category'], values = empty['Count'], hole=0.5,
    #                          marker = dict(colors = ['gray']),
    #                          hovertemplate = "볼넷 & 삼진 : None"))
    #     fig.update_layout(legend = dict(x = 0.8, y = 1, font = dict(size = 14)),
    #                       margin = dict(l = 0, r = 100),
    #                       title = '평균 삼진 대비 볼넷 비율',
    #                       title_font_size = 20)
    #     fig.add_annotation(text = f'BB/K: None', x = 0.5, y = 0.5, showarrow = False, font = dict(size = 15, family = 'sans serif', color = 'rgb(7, 30, 59)'))

    #     st.plotly_chart(fig, theme = 'streamlit')


