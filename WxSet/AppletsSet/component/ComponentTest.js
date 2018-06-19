var BehaviorTest = require('./BehaviorTest.js');

Component({
  relations: {
    'BehaviorTest.BehaviorTest': {
      type: 'descendant',
      linked: function (target) {
        console.log("c linked")
      },
      linkChanged: function (target) {
        console.log("c linkChanged")
      },
      unlinked: function (target) {
        console.log("c unlinked")
      },
      target: BehaviorTest.BehaviorTest
    }
  },
  options: {
    multipleSlots: true
  },
  behaviors: [
    BehaviorTest.BehaviorTest
  ],
  externalClasses: [
    'custom_class'
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
  methods: {
    ComponentMethod: function () {
      console.log('log from ComponentTest.js')
    }
  },
  created: function () {
    console.log("This component has been created");
  },
  attached: function () {
    console.log("This component attach to node");
  },
  ready: function () {
    console.log("The component is ready");
  },
  moved: function () {
    console.log("The component move to other");
  },
  detached: function () {
    console.log("The component is detached");
  }
})
