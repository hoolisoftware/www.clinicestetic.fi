import Illustration from '../../_CommonBlocks/Illustration'

import illustration1 from '../../../assets/components/treatmentdetail-block2-illustration1.png'
import illustration2 from '../../../assets/components/treatmentdetail-block2-illustration2.png'
import illustration3 from '../../../assets/components/page-training-fin-illustration3.jpg'
import illustration4 from '../../../assets/components/page-training-fin-illustration4.jpg'
import sofiaKazakov from '../../../assets/components/page-training-fin-sofia-kazakov.jpeg'
import Heading from '@/components/Heading';
import Container from '@/components/Container';
import {useTranslation} from "react-i18next";

export default function Block() {
    const {t, i18n} = useTranslation();
    
    return <>
        {i18n.language !== 'fin' ? (
            <>
                <Illustration
                    title={
                        <>{t("page_training_block1_title")} </>
                    }
                    content={
                        <>
                            {t("page_training_block1_p1")}
                            <br /><br />
                            {t("page_training_block1_p2")}
                            <br /><br />
                            {t("page_training_block1_p3")}
                            <br /><br />
                            {t("page_training_block1_p4")}
                            <br /><br />
                            {t("page_training_block1_p5")}
                            <br /><br />
                            {t("page_training_block1_p6")}
                        </>
                    }
                    illustration={illustration1}
                />
                <Illustration
                    title={
                        <>{t("page_training_block2_title")}</>
                    }
                    content={
                        <>
                            {t("page_training_block2_p1")}
                            <br /><br />
                            {t("page_training_block2_p2")}
                            <br /><br />
                            {t("page_training_block2_p3")}
                            <br /><br />
                            {t("page_training_block2_p4")}
                            <br /><br />
                            {t("page_training_block2_p5")}
                        </>
                    }
                    illustration={illustration2}
                    right
                />
            </>
        ) : (
            <>
                <Container>
                    <Heading center>{t('page_training_block1_title')}</Heading>
                    <center>
                        <p>
                            {t('page_training_block1_subtitle')}
                        </p>
                    </center>
                    <Heading center>{t('page_training_block1_sections_title')}</Heading>
                </Container>
                <Illustration
                    title={
                        <>{t("page_training_block1_section1_title")} </>
                    }
                    content={
                        <>
                            {t("page_training_block1_section1_p1")}
                            <br /><br />
                            {t("page_training_block1_section1_p2")}
                            <br /><br />
                            {t("page_training_block1_section1_p3")}
                            <br /><br />
                            {t("page_training_block1_section1_p4")}
                            <br /><br />
                            {t("page_training_block1_section1_p5")}
                            <br /><br />
                        </>
                    }
                    illustration={illustration1}
                />
                <Illustration
                    title={
                        <>{t("page_training_block1_section2_title")} </>
                    }
                    content={
                        <>
                            {t("page_training_block1_section2_p1")}
                        </>
                    }
                    illustration={illustration2}
                    right
                />
                <Illustration
                    title={
                        <>{t("page_training_block1_section3_title")} </>
                    }
                    content={
                        <>
                            {t("page_training_block1_section3_p1")}
                        </>
                    }
                    illustration={illustration3}
                />
                <Illustration
                    title={
                        <>{t("page_training_block1_section4_title")} </>
                    }
                    content={
                        <>
                            {t("page_training_block1_section4_p1")}
                        </>
                    }
                    illustration={illustration4}
                    right
                />
                <Container>
                    <Heading center>{t('page_training_block2_title')}</Heading>
                    <br />
                    <center>
                        <img src={sofiaKazakov} alt="sofia kazakov" />
                        <p><b>{t('page_training_block2_fullname')}</b></p>
                        <p>{t('page_training_block2_position')}</p>
                    </center>
                    <br />
                    <ul>
                        <li>{t('page_training_block2_p1')}</li>
                        <li>{t('page_training_block2_p2')}</li>
                        <li>{t('page_training_block2_p3')}</li>
                        <li>{t('page_training_block2_p4')}</li>
                    </ul>
                </Container>
            </>
        )}
    </>
}