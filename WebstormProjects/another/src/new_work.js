let log = console.log
class Person {
    name = "malik"
    age = 18

}
person = new Person()
person2 = new Person()
notPerson = new Person()

console.log(person.age)
person2.age = 99
console.log(person.age)
console.log(person2.age)
notPerson.__proto__.height = 5.5
notPerson.address = "ola street"
log(notPerson.__proto__)
log(notPerson.address)
Person.prototype.work = "working"
log(notPerson.work)
console.log(person.work)