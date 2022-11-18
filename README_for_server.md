우선 튜터링 과목 목록에 해당하는 데이터베이스를 만들었습니다.
현재 데이터베이스에 들어있는 데이터는 다음과 같습니다.
{
  "id" : "SWE2021-41",
  "name" : "OpenSource",
  "professor" : "Jo",
  "tutor" : "Ko",
  "tutee" : "Hong"
}
{
  "id" : "SWE2016-43",
  "name" : "Algorithms",
  "professor" : "JoD",
  "tutor" : "Kang",
  "tutee" : "Jung"
}
{
  "id" : "SWE3003-41",
  "name" : "Database",
  "professor" : "Nam",
  "tutor" : "Lee",
  "tutee" : "Son"
}
{
  "id" : "SWE3005-41",
  "name" : "Computer Architectures",
  "professor" : "Joh",
  "tutor" : "Chun",
  "tutee" : "Park"
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
        "tutee": "Jung",
        "tutor": "Kang"
    },
    "SWE2021-41": {
        "id": "SWE2021-41",
        "name": "OpenSource",
        "professor": "Jo",
        "tutee": "Hong",
        "tutor": "Ko"
    },
    "SWE3003-41": {
        "id": "SWE3003-41",
        "name": "Database",
        "professor": "Nam",
        "tutee": "Son",
        "tutor": "Lee"
    },
    "SWE3005-41": {
        "id": "SWE3005-41",
        "name": "Computer Architectures",
        "professor": "Joh",
        "tutee": "Park",
        "tutor": "Chun"
    }
}

#데이터 추가하기.
POST method를 사용합니다.
reqbin에서 사용해보시고, 아래 {"key" : "value"} 대신 아래와 같은 양식으로 json string을 함께 보내주세요.

{
    "id": "SWE3005-41",
    "name": "Computer Architectures",
    "professor": "Joh",
    "tutee": "Park",
    "tutor": "Chun"
}

이후에 위에서 getcourse, getallcourse를 사용하여 데이터가 추가된 것을 확인할 수 있습니다. 이때 한글로 입력하는 경우 출력이 유니코드로 나오게 됩니다.

#한편, tutee를 추가하는 기능은 아직 구현하지 않았습니다. 또한 아직은 tutee를 한명만 넣어두었습니다.

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