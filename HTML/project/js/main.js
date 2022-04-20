// 1. 타입스크립트는 필요없지만 바닐라자바스크립트는 해준다
// 자바스크립트는 빨리만들기 위해 매우 유연하지만 그만큼 위험함(EX 선언안된 변수즉시사용, 기본API인 프로토타입을 변경가능)
// ADD ECMA스크립트5(ES5)
'use strict';
console.log('Hellow World');

// 2. variable 변수(mutable)-rw(read/write)
// let (ES6) VS var(hoisting): 어디에 선언되는지 상관없이 위로 선언을 끌어올려줌

let a;
a = 4;
a = 'sin';

// 3. constant 상수(immutable)-r(only read)
// const

// 4. 데이터타입( 값 / 포인터 / 함수)
// primitive, single item: number, string, boolean, null, undefined, symbol
// object(many item), box container
// function, first-class function

// bigInt = 1234n;
console.log(`value: ${a}, type: ${typeof a}`);

// `string' + 'string` / `string: ${string}`

// false: 0, null, undefined, nan, '' true: 나머지 

// Symbol('id'); 우선순위에 상관없는 고유한 식별자 / Symbol.for('id'); 같은 고유한 식별자 / ${Symbol.description}

// object
const b = {name: 'hi', age: 22 };


// 5. 연산자 +(스트링) - / * % ** -- ++ += -= *= /= < <= > >= || && ! == != === !==

// 6. if문  1===0 ? 'yes' : 'no'  switch-case-break-default

// 7. for(let i=0; i < 10; i++) for(const i of items) while do-while

// 8. 함수 expression함수 Arrow함수 IIFE
//function log(messasge: string): number {
//	console.log(message);
//	return 0;
//} 예외-타입스크립트

function log1(message) {
	console.log(message);
	return 0;
}
const log2 = function log(message){
	console.log(message);
}

const log3 = (message) => console.log(message);

log1("에바야1");
log2("에바야2");
log3("에바야3");

(function log(message){
	console.log("에바야4");
})();


// 9. 파라미터(값/포인터) 디폴트(=) Rest(...) 함수

// 10. 배열 .length .forEach(function (i, index, array) { console.log(i); } ); = .forEach( (i, index, array) => { console.log(i); } ); join(item), reverse(), sort(함수), reduce(함수), reduceRight(함수) 
// push(unshift) / pop(shift), splice(index, num=0, item=0), concat(item) .indexOf(item) .lastIndexOf(item) .includes(item), every(함수), some(함수), map(함수), filter(함수)
{
	const fruits = ['apple', 'banana', 'orange'];
	const result = fruits.join(' and ');
	console.log(result);
}

{
	const fruits = 'apple, banana, orange';
	const result = fruits.split(',', 2);
	console.log(result);
}

{
	const array = [1,2,3,4,5];
	const result = array.reverse();
	console.log(result);
}


{
	const array = [1,2,3,4,5];
	//array.splice(0, 2); = [1, 2] 
	const result = array.slice(2, 5);
	console.log(result);
}

class Student {
	constructor(name, age, enrolled, score) {
		this.name = name;
		this.age = age;
		this.enrolled = enrolled;
		this.score = score;
	}
}

const students = [
	new Student('A', 29, true, 45),
	new Student('B', 28, false, 80),
	new Student('C', 30, true, 90),
	new Student('D', 40, false, 66),
	new Student('E', 18, true, 88),
];

{
	//const result1 = students.find(function (student, index) { return student.score === 90;} );
	const result1 = students.find( (student) => student.score === 90 );
	console.log(result1);
}

{
	//const result1 = students.filter(function (student, index) { return student.enrolled === true;} );
	const result1 = students.filter( (student) => student.enrolled === true );
	console.log(result1);
}

{
	//const result1 = students.map(function (student, index) { student.score; } ); 매핑하듯이 덮어씀
	const result1 = students.map( (student) => student.score );
	console.log(result1);
}

{
	//const result1 = students.some(function (student, index) { student.score; } );  한명이라도 있냐?
	const result1 = students.some( (student) => student.score < 50 );
	console.log(result1);

	// some = !every

	//const result2 = students.every(function (student, index) { student.score; } ); 모두 맞냐? 
	const result2 = students.every( (student) => student.score < 50 );
	console.log(result2);
}

{
	//const result1 = students.reduce(function (prev, curr) { return prev + curr.score; } ); 초기화 안하면 배열[0][1]
	const result1 = students.reduce( (prev, curr) => prev + curr.score, 0);
	console.log(result1 / students.length);
}

{
	const result1 = students
	.map( (student) => student.score )
	.join();
	console.log(result1);
}

{
	const result1 = students
	.map( (student) => student.score )
	.sort( (prev, curr) => prev - curr)
	.join();
	console.log(result1);
}
function calc(op, a, b){
	let result;
	switch(op){
		case '+':
			result = a + b;
			break;
		case '-':
			result = a - b;
			break;
		case '*':
			result = a * b;
			break;
		case '/':
			result = a / b;
			break;
		default:
			result = '연산자없음';
			break;
	
	}
	return result;
}
console.log(calc('d', 1, 2));

// 11. 클래스와 객체
class User {
	publicFd = 1;
	#privateFd = 2;

	constructor(name1, name2, value) {
		this.name1 = name1;
		this.name2 = name2;
		this.age = value;
	}
	
	get age() {
		return this._age;
	}
	set age(value) {
		if(value < 0){
			throw Error('잘못된 나이입력');
		}
		this._age = value;
	}

	static publisher = "신동민";
	static printpub() {
		console.log(User.publisher);
	}
}

const user1 = new User('아', '시발', 10);
console.log(user1.age);
User.printpub();

// 12. 다형성과 상속성 instanceof
class Shape {
	constructor(w, h, c) {
		this.width = w;
		this.height = h;
		this.color = c;
	}
	draw() {
		 console.log(`drawing ${this.color} 컬러`);
	}
	getArea() {
		return this.width * this.height;
	}
}

class Rect extends Shape {

	draw() {
		super.draw();
		console.log(`drawing ${this.color}`);
	}

	getArea() {
		return this.width * this.height / 2;
	}
}

const rect = new Rect(20, 20, 'blue');
rect.draw();
console.log(rect.getArea());

// 13. 오브젝트(클래스에 객체랑 다른거같음): {key: value}; / new Object();
const person = { name: 'ttt', age: 4 };

console.log(person.name);
person.hasjob = true;
person['hasjob'] = false;
delete person.hasjob;

// 14. 템플릿 VS 생산자 함수
const person1 = new makeob();

function makeob(name, age) {
	return {
		name,
		age,
	};
}

function Makeob(name, age) {
	this.name = name;
	this.age = age;
}

// 15. 'key' in ob / for..in(key-object) VS for..of(item-array) 

// 16. 복사- 뒤에 있는게 계속해서 앞으로 덮어짐
const person2 = Object.assign({}, person);
console.log(person2);

