<template>
  <div class="login">
    <h1>This is an login page</h1>
    <!-- 测试组建引入 -->
    <hello />

    <el-row style="margin:20px">
      <el-button @click="handler_login()">登陆接口</el-button>
      <el-button type="primary" @click="handler_registered()">注册接口</el-button>
    </el-row>
    <h1>接口返回值</h1>
    {{info}}
  </div>
</template>

<script>
import hello from "../components/HelloWorld.vue";
import { login, registered } from "../api/rules";
export default {
  data() {
    return {
      info: 212
    };
  },
  components: {
    hello
  },
  methods: {
    handler_login() {
      login().then(res => {
        this.info = res;
      });
    },
    handler_registered() {
      registered().then(res => {
        this.info = res;
      });
    }
  }
};
</script>
<style lang="scss">
</style>