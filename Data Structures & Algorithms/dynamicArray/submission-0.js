class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity; 
        this.data = {}; 
        this.length = 0;
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.data[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.data[i] = n;
        return; 
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.length === this.capacity){
            this.resize(); 
        }

        this.data[this.length] = n; 
        this.length++; 
    }

    /**
     * @returns {number}
     */
    popback() {
        if(this.length === 0){
            return undefined; 
        }

        const lastItem = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--; 
        return lastItem; 
    }

    /**
     * @returns {void}
     */
    resize() {
        const newData = {}
        for(let i = 0; i < this.length; i++){
            newData[i] = this.data[i];
        }
        this.capacity = this.capacity * 2; 
        this.data = newData;
        return;   
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.length
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
