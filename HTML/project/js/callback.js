'use strict';

// 자바는 synchronous-호이스팅후 블럭순서단위로 실행
// hoisting: var, function declaration

// async-비동기적
setTimeout(function () {
	console.log('2');
}, 1000);
console.log('3');



// sync-동기적 콜백
function printImmed(print) {
	print();
}

printImmed( () => console.log('hi'));

// async-비동기적 콜백
function printDel(print, time) {
	setTimeout(print, time);
}

printDel( () => console.log('비동기'), 2000);



class UserStorage {
	login(id, password, onSuccess, onError) {
		setTimeout(() => {
			if(id === '나' && password === '너') {onSuccess(id);}
			else {onError(new Error('잘못'));}
		}, 2000);
	}

	getRole(user, onSuccess, onError) {
		setTimeout(() => {
			if(user === '나') {onSuccess({ name: '신', role: 'admin' });}
			else {onError(new Error('접근x'));}
		}, 1000);
	}
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your pass');

/*
userStorage.login(
	id,
	password,
	user => {
		userStorage.getRole(
			user,
			userRole => { alert(`hello ${userRole.name}, have a ${userRole.role}`); },
			error => { console.log(error); }
		);
	},
	error => { console.log(error); }
);
*/


