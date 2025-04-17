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