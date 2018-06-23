% rebase('templates/base.tpl')
<div>
    <h3>アワビ特徴は、{{ sex }}, 殻長{{ length }}mm、殻幅{{ diameter }}mm、高さ{{ height }}mm、重さ{{ weight }}グラムですね</h3>
    <h3>このアワビのステイ年齢は{{ age }}歳です</h3>
</div>
<form action="/abalone" method="post">
    <fieldest>
    <legend align="left">入力フォーム</legend>
    <!-- 送信ボタン -->
    <div class="input-group">
        <input type="submit" value="年齢を当てる">
    </div>
    </fieldest>
</form>
