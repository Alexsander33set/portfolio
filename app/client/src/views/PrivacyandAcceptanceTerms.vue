<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
const language = route.params.language

const updatedAt = "18/08/2024"
</script>

<template>
    <article class="p-8 min-w-full prose lg:prose-xs dark:bg-gray-200 dark:marker:text-zinc-600">
        <template v-if="language == 'pt-br'">
            <h3 id="termos-de-privacidade-e-aceitação">Termos de Privacidade e Aceitação</h3>
            <p>Bem-vindo ao nosso aplicativo web. Priorizamos sua privacidade e estamos dedicados a proteger suas
                informações pessoais. Este documento descreve nossas práticas em relação à coleta, uso e proteção dos
                dados dos usuários.</p>
            <h4 id="coleta-de-informações">Coleta de Informações</h4>
            <ol>
                <li>
                    <p><strong>Informações Coletadas:</strong></p>
                    <ul>
                        <li>Coletamos preferências do usuário, como localização aproximada (via IP), preferências de
                            idioma e preferências de tema diretamente do navegador do usuário.</li>
                    </ul>
                </li>
                <li>
                    <p><strong>Propósito do Processamento de Dados:</strong></p>
                    <ul>
                        <li>Os dados coletados são armazenados localmente no navegador do usuário. Utilizamos essas
                            informações para personalizar e melhorar a experiência do usuário em nosso aplicativo web.
                            Não utilizamos esses dados para fins comerciais.</li>
                    </ul>
                </li>
                <li>
                    <p><strong>Segurança dos Dados:</strong></p>
                    <ul>
                        <li>Implementamos medidas rigorosas de segurança para proteger os dados contra acesso não
                            autorizado e exploração durante o processamento no navegador do usuário.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="compartilhamento-de-informações">Compartilhamento de Informações</h4>
            <ol>
                <li><strong>Compartilhamento Limitado:</strong>
                    <ul>
                        <li>Podemos compartilhar dados de geolocalização e IP com fontes externas seguras para melhorar
                            a precisão da localização ou para fins estatísticos. Esses dados são compartilhados de forma
                            anonimizada.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="direitos-do-usuário">Direitos do Usuário</h4>
            <ol>
                <li><strong>Acesso e Correção:</strong>
                    <ul>
                        <li>Os usuários podem acessar e corrigir suas informações pessoais por meio da interface do
                            aplicativo web. Como os dados são armazenados localmente, os usuários mantêm controle total
                            sobre a exclusão manual dessas informações.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="uso-de-cookies">Uso de Cookies</h4>
            <ol>
                <li><strong>Uso de Cookies:</strong>
                    <ul>
                        <li>Utilizamos cookies para otimizar a experiência do usuário em nosso aplicativo web. Os
                            cookies são anonimizados e essenciais para garantir funcionalidades básicas.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="alterações-nos-termos-de-privacidade">Alterações nos Termos de Privacidade</h4>
            <ol>
                <li><strong>Notificação de Alterações:</strong>
                    <ul>
                        <li>Os usuários serão prontamente informados sobre quaisquer alterações nos termos de
                            privacidade na próxima vez que acessarem o aplicativo web após a atualização dos termos.
                        </li>
                    </ul>
                </li>
            </ol>
            <h4 id="requisitos-de-idade">Requisitos de Idade</h4>
            <ol>
                <li><strong>Idade Mínima:</strong>
                    <ul>
                        <li>Não há restrições de idade para usar nosso aplicativo web, e não coletamos intencionalmente
                            informações pessoais de menores.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="aceitação-dos-termos">Aceitação dos Termos</h4>
            <p>Ao acessar e utilizar nosso aplicativo web, você consente com a coleta e uso de suas informações conforme
                descrito nesta política de privacidade. Se tiver dúvidas ou preocupações sobre nossos termos de
                privacidade, entre em contato conosco.</p>
            <p>Última Atualização: {{ updatedAt }}</p>

        </template>
        <template v-else>
            <h3 id="privacy-and-acceptance-terms">Privacy and Acceptance Terms</h3>
            <p>Welcome to our web application. We prioritize your privacy and are dedicated to safeguarding your
                personal
                information. This document outlines our practices regarding the collection, use, and protection of user
                data.</p>
            <h4 id="information-collection">Information Collection</h4>
            <ol>
                <li>
                    <p><strong>Collected Information:</strong></p>
                    <ul>
                        <li>We gather user preferences such as approximate location (via IP), language preferences, and
                            theme preferences directly from the user&#39;s browser.</li>
                    </ul>
                </li>
                <li>
                    <p><strong>Purpose of Data Processing:</strong></p>
                    <ul>
                        <li>The collected data is stored locally within the user&#39;s browser. We utilize this
                            information
                            to personalize and enhance the user experience on our web application. We do not use this
                            data
                            for commercial purposes.</li>
                    </ul>
                </li>
                <li>
                    <p><strong>Data Security:</strong></p>
                    <ul>
                        <li>We implement stringent security measures to protect data against unauthorized access and
                            exploitation during processing within the user&#39;s browser.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="information-sharing">Information Sharing</h4>
            <ol>
                <li><strong>Limited Sharing:</strong>
                    <ul>
                        <li>We may share geolocation and IP data with secure external sources to enhance location
                            accuracy
                            or for statistical purposes. This data is shared in anonymized form.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="user-rights">User Rights</h4>
            <ol>
                <li><strong>Access and Correction:</strong>
                    <ul>
                        <li>Users can access and correct their personal information through the web application
                            interface.
                            Since data is stored locally, users retain full control over manually deleting this
                            information.
                        </li>
                    </ul>
                </li>
            </ol>
            <h4 id="use-of-cookies">Use of Cookies</h4>
            <ol>
                <li><strong>Cookies Usage:</strong>
                    <ul>
                        <li>We utilize cookies to optimize the user experience on our web application. Cookies are
                            anonymized and essential for ensuring core functionalities.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="changes-to-privacy-terms">Changes to Privacy Terms</h4>
            <ol>
                <li><strong>Notification of Changes:</strong>
                    <ul>
                        <li>Users will be promptly notified of any revisions to the privacy terms upon their next login
                            to
                            the web application following the terms update.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="age-requirements">Age Requirements</h4>
            <ol>
                <li><strong>Minimum Age:</strong>
                    <ul>
                        <li>There are no age restrictions for using our web application, and we do not intentionally
                            collect
                            personal information from minors.</li>
                    </ul>
                </li>
            </ol>
            <h4 id="acceptance-of-terms">Acceptance of Terms</h4>
            <p>By accessing and utilizing our web application, you consent to the collection and use of your information
                as
                outlined in this privacy policy. Should you have any queries or concerns regarding our privacy terms,
                please
                do not hesitate to contact us.</p>
        </template>
    </article>
</template>