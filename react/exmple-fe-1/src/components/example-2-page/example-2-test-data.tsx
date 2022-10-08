
const testDataSize: number = 250;

export const testData = new Array(testDataSize).fill(0).map((_, i) => i + 1).map(i => ({
    key: i.toString(),
    name: `Ettore ${i}`,
    phone: `333-${99999 * (i + 1)}`,
}))