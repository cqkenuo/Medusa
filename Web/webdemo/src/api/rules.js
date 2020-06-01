import {
    post
} from '../util/request'
import {
    URL_POST_LOGIN,
    URL_POST_REGISTERED
} from './url'

// 登陆接口
export async function login(params) {
    let response = await post(URL_POST_LOGIN, params, {
        headers: {}
    })
    return response
}

// 登陆接口
export async function registered(params) {
    let response = await post(URL_POST_REGISTERED, params, {
        headers: {}
    })
    return response
}
