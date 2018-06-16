module.exports = {
  "BehaviorTest": Behavior({
    behaviors: [],
    properties: {
      BehaviorProperty: {
        type: String,
        value: '20',
        observer: function (newVal, oldVal, changedPath) {
          console.log("BehaviorTest改变属性", newVal, oldVal, changedPath)
        }
      }
    },
    data: {
      BehaviorData: "BehaviorData"
    },
    attached: function () {
      console.log("The Behavior is being made")
    },
    methods: {
      BehaviorMethod: function () {
        console.log('log from my-behavior.js')
      }
    }
  })
}