# appstore-privacy

Google Play 앱들의 개인정보처리방침 페이지. GitHub Pages(공개 저장소)로 서비스한다.

- 공개 URL: `https://dybarogo.github.io/appstore-privacy/<slug>.html`
- 앱 추가: `python make_page.py <slug> <package> "<이름 KO>" "<이름 EN>" <문의 이메일> [시행일]` → `<slug>.html` 생성 + `index.html` 목록 갱신 → 커밋·푸시
- 본문 수정은 `template.html`에서 하고 각 앱 페이지를 다시 생성한다.
- 앱이 서버·분석 SDK·권한을 추가로 쓰면 그 앱 페이지의 1번·3번 항목을 수정해야 한다(수집 항목이 Play 데이터 안전 양식과 일치해야 함).
