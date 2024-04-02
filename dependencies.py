# 인증 관련 추가 >> 토큰 기반으로 유저 네임값을 가져올 수 있도록 한다.

# 테스트를 위한 사용자 정보
users = {
    1: {'username': '111@111.com'},
    2: {'username': '222@111.com'},
    3: {'username': '333@111.com'}
}


def get_username(token: str):
    # users정보를 토큰으로 간주
    user_id = int(token)
    user = users.get(user_id)
    return user['username']