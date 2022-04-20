//JSON- javascript object notation

// 1. ob to json           .stringify

let json = JSON.stringify(true);
console.log(json);

const rabbit = {
	name: 'tori',
	color: 'white',
	size: null,
	birthDate: new Date(),
	//symbol: Symbol('id'),
	jump: () => {
		console.log(`${name} can jump`);
	},
};


json = JSON.stringify(rabbit, ['naem', 'color']);
console.log(json);

json = JSON.stringify(rabbit, (key, value) => {
	//console.log(`key: ${key}, val: ${value}`);
	return key === 'name' ? '토끼' : value; 
});
console.log(json);

// 2. json to ob           .parse

const obj = JSON.parse(json, (key, value) => {
	//console.log(`key: ${key}, val: ${value}`);
	return key === 'birthDate' ? new Date(value) : value; 
});
console.log(obj);
rabbit.jump();
//obj.jump();

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());




















