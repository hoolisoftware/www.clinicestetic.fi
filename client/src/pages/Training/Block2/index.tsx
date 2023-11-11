import css from './index.module.scss'

import Card, {CardContent, CardTitle} from '../../../components/Card'
import {useTranslation} from "react-i18next";

export default function Block() {
    const {t, i18n} = useTranslation();
    

    return <div className={css.container}>
        { i18n.language !== 'fin' ? (
            <>
                <div className={css.section}>
                    <Card>
                        <CardContent>
                            {t("page_training_block3_card1_p1")}
                            <br /><br />
                            {t("page_training_block3_card1_p2")}
                            <br /><br />
                            {t("page_training_block3_card1_p3")}
                            <br /><br />
                            {t("page_training_block3_card1_p4")}
                            <br /><br />
                            {t("page_training_block3_card1_p5")}
                            <br /><br />
                            {t("page_training_block3_card1_p6")}
                            <br /><br />
                            {t("page_training_block3_card1_p7")}
                            <br /><br />
                            {t("page_training_block3_card1_p8")}
                            <br /><br />
                            {t("page_training_block3_card1_p9")}
                            <br /><br />
                            {t("page_training_block3_card1_p10")}
                            <br /><br />
                            {t("page_training_block3_card1_p11")}
                            <br /><br />
                            {t("page_training_block3_card1_p12")}
                            <br /><br />
                            {t("page_training_block3_card1_p13")}
                            <br /><br />
                            {t("page_training_block3_card1_p14")}
                        </CardContent>
                    </Card>
                </div>
                <div className={css.section}>
                    <div className={css.cards}>
                        <Card>
                            <CardContent>
                                <CardTitle>{t("page_training_block3_card2_title")}</CardTitle>
                                {t("page_training_block3_card2_p1")}
                                <br /><br />
                                {t("page_training_block3_card2_p2")}
                                <br /><br />
                                {t("page_training_block3_card2_p3")}
                                <br /><br />
                                {t("page_training_block3_card2_p4")}
                                <br /><br />
                                {t("page_training_block3_card2_p5")}
                                <br /><br />
                                {t("page_training_block3_card2_p6")}
                            </CardContent>
                        </Card>
                        <Card>
                            <CardContent>
                                <CardTitle>{t("page_training_block3_card3_title")}</CardTitle>
                                {t("page_training_block3_card3_p1")}
                                <br /><br />
                                {t("page_training_block3_card3_p2")}
                                <br /><br />
                                {t("page_training_block3_card3_p3")}
                                <br /><br />
                                {t("page_training_block3_card3_p4")}
                                <br /><br />
                                {t("page_training_block3_card3_p5")}
                            </CardContent>
                        </Card>
                    </div>
                </div>
                <div className={css.section}>
                    <div className={css.cards}>
                        <Card>
                            <CardContent>
                                <CardTitle>{t("page_training_block3_card4_title")}</CardTitle>
                                {t("page_training_block3_card4_p1")}
                            </CardContent>
                        </Card>
                        <Card>
                            <CardContent>
                                <CardTitle>{t("page_training_block3_card5_title")}</CardTitle>
                                {t("page_training_block3_card5_p1")}
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </>
        ) : ('') }
    </div>
}