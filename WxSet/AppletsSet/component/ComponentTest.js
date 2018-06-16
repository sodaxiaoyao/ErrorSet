var BehaviorTest = require('./BehaviorTest.js')


Component({
  behaviors: [
    BehaviorTest.BehaviorTest
  ],

  properties: {
    ComponentProperty: {
      type: String,
      value: '30',
      observer: function (newVal, oldVal, changedPath) {
        console.log("ComponentProperty改变属性", newVal, oldVal, changedPath)
      }
    }
  },
  data: {
    ComponentData: "ComponentData"
  },


  attached: function () {
    console.log("The Component is being made")
  },
  methods: {
    ComponentMethod: function () {
      console.log('log from ComponentTest.js')
    }
  },

  options: {
    multipleSlots: true
  },
  externalClasses: [
    'my-class'
  ],

})