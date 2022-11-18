우선 튜터링 과목 목록에 해당하는 데이터베이스를 만들었습니다.
현재 데이터베이스에 들어있는 데이터는 다음과 같습니다.
튜터와 튜티는 사람 이름이 아닌, 학번으로 바꿨습니다. 
{
  "id" : "SWE2021-41",
  "name" : "OpenSource",
  "professor" : "Jo",
  "tutor" : "2020312141",
  "tutee" : "2021312345"
}
{
  "id" : "SWE2016-43",
  "name" : "Algorithms",
  "professor" : "JoD",
  "tutor" : "2021313425",
  "tutee" : "2019311943"
}
{
  "id" : "SWE3003-41",
  "name" : "Database",
  "professor" : "Nam",
  "tutor" : "2020311412",
  "tutee" : "2021313230,2016311123,2021314567"
}
{
  "id" : "SWE3005-41",
  "name" : "Computer Architectures",
  "professor" : "Joh",
  "tutor" : "2020314539",
  "tutee" : "2022311195"
}

#데이터베이스 주소
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev

해당 주소뒤에 다른 단어(?)를 붙임으로써 특정 기능을 수행할 수 있습니다. 데이터베이스에 데이터를 집어넣거나, 빼오는 기능들이요.

#test
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/test
해당 method는 get method입니다. GET Method의 경우 바로 접속해도 상관없습니다만, 아래 reqbin링크에서도 같은 결과를 확인할 수 있습니다.

#데이터 확인하기
특정 과목의 데이터를 확인하고자 하는 경우, /dev 뒤에 /getcourse를 입력합니다. 이때, 'POST' Method를 이용하며, 과목코드(id)를 함께 보내야합니다. 

https://reqbin.com/post-online

에 들어가서 URL 입력란에 
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/getcourse
를 입력하고, 링크 옆의 GET/POST/PUT/PATCH/~~를 선택하는 란에서 POST를 선택하세요.

아래 {"key" : "value"}를 지우고 
{"id" : "SWE2016-43"}과 같이 입력해보세요.

모든 과목의 데이터를 얻고자 하는 경우
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/getallcourse
로 들어가거나
위의 reqbin 링크에서 위 링크를 입력하고, GET을 선택해보세요. 아래 결과를 얻을 수 있습니다.

{
    "SWE2016-43": {
        "id": "SWE2016-43",
        "name": "Algorithms",
        "professor": "JoD",
        "tutee": ["2019311943"],
        "tutor": "2021313425"
    },
    "SWE2021-41": {
        "id": "SWE2021-41",
        "name": "OpenSource",
        "professor": "Jo",
        "tutee": ["2021312345'", "'2022313547"],
        "tutor": "2020312141"
    },
    "SWE3003-41": {
        "id": "SWE3003-41",
        "name": "Database",
        "professor": "Nam",
        "tutee": ["2021313230", "2016311123", "2021314567"],
        "tutor": "2020311412"
    },
    "SWE3005-41": {
        "id": "SWE3005-41",
        "name": "Computer Architectures",
        "professor": "Joh",
        "tutee": ["2022311195"],
        "tutor": "2020314539"
    }
}

#데이터 추가하기.
POST method를 사용합니다.
reqbin에서 사용해보시고, 아래 {"key" : "value"} 대신 아래와 같은 양식으로 json string을 함께 보내주세요.

{
    "id": "SWE2020-41",
    "name": "Computer Engineering",
    "professor": "Woo",
    "tutee": "2021312323,2019312396,2021313782",
    "tutor": "2018310142"
}
(아직 추가되지 않은 데이터입니다.)

이후에 위에서 getcourse, getallcourse를 사용하여 데이터가 추가된 것을 확인할 수 있습니다. 이때 한글로 입력하는 경우 출력이 유니코드로 나오게 됩니다.

User 목록에 있는 사람은 다음과 같습니다.

#User 추가
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/adduser
에서 post request를 보냅니다.
reqbin에서 위 링크를 입력하고 아래와 같이 입력해보세요.
{
    "id" : "2019311241",
    "name" , "Hun"
}
(추가되지 않은 데이터입니다.)

현재 User 목록은 다음과 같습니다.
{
    "2016311123": {
        "name": "Arul",
        "user_id": "2016311123"
    },
    "2019311943": {
        "name": "Jin",
        "user_id": "2019311943"
    },
    "2020311412": {
        "name": "Bagga",
        "user_id": "2020311412"
    },
    "2020312141": {
        "name": "Jung",
        "user_id": "2020312141"
    },
    "2020314539": {
        "name": "Kang",
        "user_id": "2020314539"
    },
    "2021312345": {
        "name": "Dong",
        "user_id": "2021312345"
    },
    "2021313230": {
        "name": "Boas",
        "user_id": "2021313230"
    },
    "2021313425": {
        "name": "Yu",
        "user_id": "2021313425"
    },
    "2021314567": {
        "name": "Chun",
        "user_id": "2021314567"
    },
    "2022311195": {
        "name": "Won",
        "user_id": "2022311195"
    },
    "2022313547": {
        "name": "Griffiths",
        "user_id": "2022313547"
    }
}

#login
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/login
로 post request를 보냅니다.
reqbin에서 위 링크를 입력하고 아래와 같이 입력해보세요.
{
    "name": "Griffiths",
    "user_id": "2022313547"
}
user_id와 name이 잘 일치하면 {success : True}를, 잘 일치하지 않을 경우 {success : False}를 반환합니다.

한편, tutee를 추가하는 기능도 구현했습니다.
https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev/addtutee
로 post request를 보냅니다. 
reqbin에서 위 링크를 입력하고 course_id와 tutee의 학번을 입력합니다.
{
    "tutee" : "(tutee 학번)",
    "id" : "(Course_id)"
}

tutee가 해당 튜터링에 존재하지 않고, 튜티 인원이 5명을 넘지 않으면 튜티 명단에 추가되며, {success : True}를 반환합니다.
그렇지 않다면 {success : False}를 반환합니다.(해당 튜터링이 존재하지 않는 경우도 포함)


이외에 JS에서 서버에서 나온 출력을 어떻게 받아오는지는 저도 아직 잘 모르겠습니다. fetch를 잘 활용하면 될 거 같은데요, 저는 잘 안 되는거 같네요. 위에 적어놓은 것 한번씩 실행해보시고 확인해주세요.


login test 계정
{
    "2017310820": {
        "password": "asdfgh",
        "user_id": "2017310820"
    },
    "2020312141": {
        "password": "qwerty",
        "user_id": "2020312141"
    },
    "2020315791": {
        "password": "zxcvbn",
        "user_id": "2020315791"
    }
}