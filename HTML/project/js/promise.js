'use strict';

// Promise=쓰레드랑같은원리: 비동기객체 1.상태 2.생산자/소비자
// state: pending -> fulfilled or rejected
// 네트워크 정보, 파일 읽기유용


// 생산자-run처럼 선언하자마자 바로실행(executor=auto)
const promise = new Promise((resolve, reject) => {
	console.log('');
	setTimeout(()=>{
		//resolve('프로미스');	
		reject(new Error('에러임'));
	}, 2000);
});

// 소비자: then, catch, finally
promise
	.then(value => {
		console.log(value);
	})
	.catch(error => {
		console.log(error);
	})
	.finally(()=>{
		console.log('끝');
	});



// 예제
const fetch = new Promise((resolve, reject) => {
	console.log('');
	setTimeout(()=>{
		resolve(1);	
	}, 1000);
});


fetch
	.then(num => num*2)
	.then(num => num*3)
	.then(num => { return new Promise((resolve, reject) =>  { setTimeout(() => resolve(num-1), 1000);});
	})
	.then(num => console.log(num));


// 예외처리
const getHen1 = () =>
	new Promise((resolve, reject) => {
		setTimeout(()=> resolve('아기'), 1000);
	});

const getHen2 = hen1 =>
	new Promise((resolve, reject) => {
		setTimeout(()=> 
			//resolve(`${hen1} => 청소년`)
			reject(`${hen1} => 청소년`)
			, 1000);
	});

const getHen3 = hen2 =>
	new Promise((resolve, reject) => {
		setTimeout(()=> resolve(`${hen2} => 성인`), 1000);
	});

getHen1()
	.then(hen => getHen2(hen))
	.catch(error => {return '머임';})
	.then(hen => getHen3(hen))
	.then(console.log);


class UserStorage {
	login(id, password) {
		return new Promise((resolve, reject) => {
			setTimeout(() => {
				if(id === '나' && password === '너') {resolve(id);}
				else {reject(new Error('잘못'));}
			}, 2000);
		});
	}

	getRole(user) {
		return new Promise((resolve, reject) => {
			setTimeout(() => {
				if(user === '나') {resolve({ name: '신', role: 'admin' });}
				else {reject(new Error('접근x'));}
			}, 1000);
		});
	}
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your pass');

userStorage
	.login(id, password)
	.then(userStorage.getRole)
	.then(user => alert(`hello ${user.name}, have a ${user.role}`) )
	.catch(console.log);


// async 와 await
function delay(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

function fetchUser() {
	//do network reqeust in 10secs....
	//return 'async';
	// 순차처리=동기적으로 인해 기달려야함 하지만 프로미스로 비동기실행하며 then으로 언제가는 실행시켜줌
	return new Promise( (resolve, reject) => {
		resolve('async');
	});
}

async function fetchUser1() {
	//do network reqeust in 10secs....
	// 자동으로 프로미스로 만들어줌
	await delay(3000);
	return 'async';
}

const async = fetchUser1();
async.then(console.log);
console.log(async);

async function geta() {
	await delay(2500);
	return 'apple';
}
async function getb() {
	await delay(2500);
	return 'banana';
}
async function Fruits() {
	//const apple = await geta(); 이러면 결국 비동기적임 try-catch도사용해야함
	//const banana = await getb();

	const applePro = geta(); 
	const bananaPro = getb();
	const apple = await applePro;
	const banana = await bananaPro;
	return `${apple}  +  ${banana}`;
}

function Fruits1() {
	//return Promise.all([geta(), getb()])	
	//.then(fruits => fruits.join(' + '));	//모두되면 실행

	return Promise.race([geta(), getb()]);  //경쟁해서 먼저된거
}

const async1 = Fruits1();
async1.then(console.log);



// 결과적으로 중첩이 되면 async고 병렬적이면 Promise인듯
