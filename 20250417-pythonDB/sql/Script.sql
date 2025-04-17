show databases;
use test;

CREATE TABLE test.app_user (
	id BIGINT auto_increment NOT NULL PRIMARY KEY COMMENT '아이디',
	name varchar(100) NOT NULL COMMENT '이름',
	age INT NOT NULL COMMENT '나이',
	create_dt DATETIME NULL COMMENT '생성 날짜',
	update_dt DATETIME NULL COMMENT '변경날짜'
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

drop table test.app_user;
-- gui에서 auto commit를 켜거나 끌수 이음 메뉴방에서 T 모양 아이콘 그거에 따라 커밋 롤백 버튼이 활성화/비활성화 됨 굉장히 중요한 기능 이러한 기능을 이용해서 안전성을 올림
-- crud중에 read
select * from app_user;
-- crud중에 create
insert into app_user (name,age) values ('홍길동',26);
insert into app_user (name,age) values ('이순신',45);
insert into app_user (name,age,create_dt) values ('강감찬',45,'2025-04-17');

rollback;
commit;

-- crud중에 update
update app_user set age = 58 where id = 5;
-- crud중에 delete
delete from app_user where id = 6;

select * from  국외_전체_국가_현황표;
-- ALTER TABLE 국외_전체_국가_현황표 MODIFY COLUMN 날짜 DATE NOT NULL;

select * from app_user order by name;