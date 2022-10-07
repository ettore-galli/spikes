
const testDataSize: number = 200;
export const testData = new Array(testDataSize).fill(0).map((_, i) => i + 1).map(i => ({
    key: i.toString(),
    name: `Edrward ${i}`,
    age: 32,
    address: `London Park no. ${i}`,
}))