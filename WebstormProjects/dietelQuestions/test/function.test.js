const {sum, subtract} = require("./function")
// const expect = require("expect");

// description of what the tes t is about
test("Sum 2 + 5 is equal 7", () =>{
    expect(sum(2,5)).toBe(7);
})

test("Subtract 5 - 2 is equal 3", () =>{
    expect(subtract(5,2)).toBe(3);
})
