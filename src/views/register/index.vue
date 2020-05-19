<template>
  <div>
  <div class="login-container">
   <title>注册-Medusa</title>
    </div>
    <el-form-item prop="username">
      <span class="svg-container">
        <svg-icon icon-class="user" />
      </span>
      <el-input
        ref="username"
        placeholder="Username"
        name="username"
        type="text"
        tabindex="1"
        autocomplete="on"
      />
    </el-form-item>
    <div class="input_group">
      <label>昵称：</label>
      <input class="myinput" type="text" placeholder="请输入昵称" v-model="usershowname" />
    </div>
    <div class="input_group">
      <label>用户名：</label>
      <input class="myinput" type="text" placeholder="请输入用户名" v-model="username" />
    </div>
    <div class="input_group">
      <label>密码：</label>
      <input class="myinput" type="password" placeholder="请输入密码" v-model="userpass" />
    </div>
    <div class="input_group">
      <label>请确认密码：</label>
      <input class="myinput" type="password" placeholder="请输入密码" v-model="userpassagain" />
    </div>
    <div class="input_group">
      <label>邮箱：</label>
      <input class="myinput" type="password" placeholder="请输入邮箱" v-model="useremail" />
    </div>
    <button class="ok_btn" @click="register">注册</button>
    <button class="cancel_btn" @click="backLogin">{{backText}}</button>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        backText: '返回',
        username: '',
        userpass: '',
        userpassagain: '',
        useremail: '',
        usershowname: ''
      }
    },
    methods: {
      backLogin() {
        this.$router.replace('/login')
      },
      register() {
        var vm=this;
        this.$reqs.post('users/register', {
          username: this.username,
          password: this.password,
          showname: this.usershowname,
          email: this.useremail
        }).then(function (res) {
          if (res.data.status !== true) {
            Toast(res.data.errMsg);
          } else {
            let instance = Toast('注册成功，请登录!');
            setTimeout(() => {
              instance.close();
              vm.$router.replace('/login');
            }, 2000);
          }
        })
      }
    }
  }
</script>
<style lang="scss">

// $bg:#283443;
// $light_gray:#fff;
// $cursor: #fff;
$bg:#000000;
$light_gray:#000;
$cursor: #000;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    // color: #454545;

    color: #000;
  }
}
</style>

<style lang="scss" scoped>
$bg:#EEEED1;
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #000;
    // color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: #000;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: #000;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>
