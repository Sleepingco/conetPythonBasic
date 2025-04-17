#  elastic searc: 검색용 한글도 잘됨 nosql database
# 데이터의 무결성을 바라는게 아니라 빠른 검색과 비정형 데이터를 다루는 데이터
# Http Method get(조회),post(조작,insert,update,delete),put(update),delete(삭제),option,patch
# {
#     "name":"홍길동",
#     "age":25,
#     "friend":[
#         "name":"강감찬",
#     ]
# }
# https://coralogix.com/blog/42-elasticsearch-query-examples-hands-on-tutorial/
# Welcome to the Dev Tools Console!
#
# You can use Console to explore the Elasticsearch API. See the Elasticsearch API reference to learn more:
# https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html
#
# Here are a few examples to get you started.


# # Create an index
# PUT /my-index


# # Add a document to my-index
# POST /my-index/_doc
# {
#     "id": "park_rocky-mountain",
#     "title": "Rocky Mountain",
#     "description": "Bisected north to south by the Continental Divide, this portion of the Rockies has ecosystems varying from over 150 riparian lakes to montane and subalpine forests to treeless alpine tundra."
# }


# # Perform a search in my-index
# GET /my-index/_search?q="rocky mountain"

# 엘라스틱 서치는 풀택스트 서치에 아주 좋지만 RDB는 쥐약 글자마다 토크나이저로 잘라서 인덱스 넣어서 찾는게 가능
# 검색 옵션에 and,or,minimum,multi 등 다양함

from elasticsearch import Elasticsearch
# 첫 ID는 'elastic'이며, 비밀번호는 처음 주어진 비밀번호를 변경가능함
ELASTIC_ID = "elastic"
ELASTIC_PASSWORD = "KyOXsSI0swLp9RxQD4gj"

# # client instance 생성
client = Elasticsearch(
    "https://localhost:9200",   # endpoint
    ca_certs="C:/Users/main/Desktop/elasticsearch/config/certs/http_ca.crt",
    basic_auth=(ELASTIC_ID, ELASTIC_PASSWORD)
)

# 접속이 잘 되었다면 아래 코드로 확인가능함
# print(client.info())
# {'name': 'instance-0000000000', 'cluster_name': ...}
# 인덱스 생성하기
# result = client.indices.create(index="my_index")
# print(result)
# 문서 생성하기
# result = client.index(
#     index="my_index",
#     id="my_document_id",
#     document={
#         "field1":"value1",
#         "field2":"value2"
#     }
# )
# print(result)
# 문서 조회하기
# result = client.get(index="my_index",id="my_document_id")
# print(result)
# 문서 검색하기
# result = client.search(index="my_index", query={
#     "match": {
#         "field1": "value1"
#     }
# })
# print(resuslt)

# search는 여러개의 문서들을 검색한다.
# "my_index" 인덱스에 쿼리를 날려 문서를 검색할 수 있다.
# "match"는 쿼리 종류를 의미한다.
# match: 풀 텍스트에서 해당 단어를 검색한다. (OR 검색)
# match_all: 모든 문서를 검색한다.
# 검색 개수를 제한하려면 search 함수의 매개변수로 size = n을 추가할 수 있다.
# 예시에서는 field1에 value1을 포함하는 문서들이 검색되며, 해당 문서들은 resp['hits']['hits'] 안에 리스트 형태로 문서들이 담겨있다.
# 문서 수정하기

# client.update(index="my_index", id="my_document_id", doc={
#     "field1":"new value1",
#     "new_field":"new value2s",
# })
# "my_index" 인덱스의 문서 ID가 "my_document_id"인 문서를 찾아 doc의 내용으로 수정한다.
# "field1": "new value1" 코드는 "field1" 필드의 값을 "new value1"로 변경하는 것을 의미한다.
# "new_field": "new value2" 코드는 "new_field"라는 새로운 필드를 추가하고, 그 값을 "new value2"로 설정하는 것을 의미한다.

# result = client.get(index="my_index",id="my_document_id")
# print(result)

# result = client.delete(index="my_index", id="my_document_id")
# print(result)
# https://code-angie.tistory.com/161 출처

# from elasticsearch import Elasticsearch

# client = Elasticsearch(
#     "https://localhost:9200",
#     ca_certs="C:/Users/main/Desktop/elasticsearch/config/certs/http_ca.crt",
#     basic_auth=("elastic", "KyOXsSI0swLp9RxQD4gj")
# )

# # 인덱스 생성 (이미 존재할 수도 있으므로 try-except)
# try:
#     client.indices.create(index="my_index")
#     print("✅ 인덱스 생성 완료")
# except Exception as e:
#     print("⚠️ 인덱스 이미 존재 또는 오류:", e)

# # 문서 생성
# client.index(
#     index="my_index",
#     id="my_document_id",
#     document={
#         "field1": "value1",
#         "field2": "value2"
#     }
# )
# print("📄 문서 생성 완료")

# # 문서 조회
# doc = client.get(index="my_index", id="my_document_id")
# print("🔍 조회 결과:", doc)

# # 문서 삭제 전 확인 후 삭제
# if client.exists(index="my_index", id="my_document_id"):
#     result = client.delete(index="my_index", id="my_document_id")
#     print("🗑️ 삭제 완료:", result)
# else:
#     print("⚠️ 삭제하려는 문서가 존재하지 않음.")
