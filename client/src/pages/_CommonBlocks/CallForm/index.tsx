import axios from 'axios'
import { useDispatch, useSelector } from 'react-redux'
import { useMutation } from 'react-query'

import { RootState } from '@/app/store'
import { toggleModalRecaptcha } from '@/features/modal/modalReducer'
import css from './index.module.scss'
import { API_URL } from '@/config'
import arrow from '@/assets/components/home-block7-arrow.png'
import bgLayer1 from '@/assets/components/home-block7-bglayer1.png'
import bgLayer2 from '@/assets/components/home-block7-bglayer2.png'
import bgLayer3 from '@/assets/components/home-block7-bglayer3.png'
import Heading from '@/components/Heading'
import Button from '@/components/Button'
import FieldPhone from '@/components/FieldPhone'
import {useTranslation} from "react-i18next";


export default function Block(){
    const dispatch = useDispatch()
    const recaptcha = useSelector((state: RootState) => state.data.recaptcha)
    const {t} = useTranslation();
    const mutation = useMutation({
        mutationFn: async (newCallForm: FormData) => {
            return axios.post(`${API_URL}booking/form-phone/`, newCallForm)
        },
        onSuccess: () => {
            alert(t('block_form_call_form_success_alert'))
        },
        onError: () => {
            alert('block_form_call_form_captcha_alert')
        }
    })

    return <div className={css.block}>
        <img className={css.bgLayer3} src={bgLayer3} alt="bgLayer3" />
        <img className={css.bgLayer2} src={bgLayer2} alt="bgLayer2" />
        <img className={css.bgLayer1} src={bgLayer1} alt="bgLayer1" />
        <div className={css.container}>
            <Heading center>
                <div className={css.heading}>{t("block_form_call_title")}</div>
            </Heading>
            <div className={css.subheading}>{t("block_form_call_text")}</div>
            <div className={css.form}>
                <form action="" onSubmit={ e => {e.preventDefault(); mutation.mutate(new FormData(e.currentTarget))} }>
                    <div className={css.formInner}>
                            <FieldPhone
                                className={css.formInput}
                                fullWidth
                                disabled={mutation.isSuccess}
                                placeholder={t("block_form_call_form_phone")}
                                type='text'
                                name='phone_number'
                                required
                            />
                            <input type="text" hidden name='recaptcha' value={recaptcha as string}/>
                            <Button
                                disabled={mutation.isSuccess}
                                className={css.formButton}
                                fullWidth
                                onClick={ (e) => {
                                    if (!recaptcha) {
                                        e.preventDefault()
                                        dispatch(toggleModalRecaptcha()) 
                                    }
                                }}
                            >
                                {t("block_form_call_form_button")}
                                <img className={css.formButtonArrow} src={arrow} alt="arrow" />
                            </Button>
                    </div>
                </form>
            </div>
        </div>
    </div>
}