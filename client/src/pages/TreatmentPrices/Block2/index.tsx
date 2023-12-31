import css from './index.module.scss'

import { Link } from 'react-router-dom'

import arrow from '../../../assets/components/treatmentprices-arrow.png'

import { Service } from '@/hooks/use-query/services'

import Heading from '../../../components/Heading'
import Card, {CardContent} from '../../../components/Card'
import Container from '../../../components/Container'
import Button from '../../../components/Button'

import Item from './Item'
import {useTranslation} from "react-i18next";


interface props
{
    treatment: Service 
}


export default function Block(props: props) {

    const {t} = useTranslation();
    return <Container>
        <div className={css.heading}>
            <Heading center >{t("page_treatment_block1_title")}</Heading>
        </div>
        <div className={css.section}>
            <div className={css.sectionBlock}>
                <Item treatment={props.treatment}/>
            </div>
            <div className={css.sectionBlock}>
                <Card>
                    <CardContent>
                        <div className={css.cardContent}>
                            <div className={css.cardTitle}>{t("sidebar_consultation_title")}</div>
                            <div className={css.cardText}>{t("sidebar_consultation_text")}</div>
                            <Link to='/book/' className={css.button}>
                                <Button fullWidth>
                                    {t("sidebar_consultation_button")}
                                    &nbsp;
                                    <img src={arrow} alt="arrow" />
                                </Button>
                            </Link>
                        </div>
                    </CardContent>
                </Card>
            </div>
        </div>
    </Container>
}