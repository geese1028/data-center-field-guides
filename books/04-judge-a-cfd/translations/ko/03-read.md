영어판을 AI 보조로 번역한 것이다.

# 3. 공기역학과 CFD 보고서 판독법

## 현장 계측과 수치 모델의 대조 원칙

데이터센터의 기류 및 열환경을 평가하는 전산유체역학(CFD)에서 **공급 공기 분배 지수($\text{SHI} < 0.15$), 환기 열회수 지수($\text{RHI} > 0.85$), 랙 냉각 지수($\text{RCI}_{\text{HI}} \ge 96\%$) 및 아르키메데스 수($\text{Ar}$)를 통한 부력 대 관성 지배 판정**은(는) 설비 신뢰성을 좌우하는 핵심 기술 규율이다. 교정된 물리 계측기를 통한 현장 벤치마킹 없이 제출된 시뮬레이션 보고서는 편미분방정식으로 그린 가설에 불과하며, 실제 운영 홀의 인수 증거로 서명해서는 안 된다.

![3. 공기역학과 CFD 보고서 판독법](../figures/fig-02-underfloor-plenum-hydraulics.png)

$$P_{\text{total}} = P_{\text{static}} + \frac{1}{2} \rho v^2$$

현장 검증팀은 서버 팬 곡선 $P$-$Q$와 컨테인먼트 차압($+2.5\,\text{Pa} \sim +12.0\,\text{Pa}$)의 연성 해석을(를) 동시에 취득하여 수치 솔버 내 프로브 좌표($\pm 50\,\text{mm}$ 이내)와 일대일로 대조해야 한다. 온도장 일치만 확인하고 풍량이나 정압차($\Delta P$) 검증을 생략하면, 열부하와 풍량 모두가 동일한 비율로 과소평가된 중대한 모델 결함을 놓치게 된다.

> *"물리적 실측 벤치마킹(Sheet 1)과 수치 경계 조건 공개(Sheet 2)가 동반되지 않은 CFD 보고서는 미검증 설계 가설로 취급되며, 어떠한 운영 변경이나 용량 승인의 근거도 될 수 없다."*

## 열유체역학 지배방정식과 계측 허용 오차

고밀도 AI 클러스터 및 하이브리드 냉각(액체+공기) 홀에서는 전기 입력($P_{\text{elec}}$)에서 2차 냉각 루프의 엔탈피 흡수량($Q_{\text{liquid}}$)을 차감한 현열 잔차($Q_{\text{air}}$)만이 실내 공기로 방출된다. 명판 정격(PSU 합산치)을 그대로 열원으로 투입하면 40%~80%에 달하는 허수 열부하가 발생하여 불필요한 설비 투자나 잘못된 냉각 설정을 초래한다.

![3. 공기역학과 CFD 보고서 판독법](../figures/fig-03-containment-leakage-aerodynamics.png)

$$\left| \frac{\sum \dot{m}_{\text{supply}} - \sum \dot{m}_{\text{exhaust}}}{\sum \dot{m}_{\text{supply}}} \right| \times 100\% \le 0.10\%$$

| 감사 파라미터 | 물리 계측 / 수치 지표 | 합격 기준 (허용 오차) | 거부 트리거 (불합격 조건) |
| :--- | :--- | :--- | :--- |
| **랙 흡기 온도 (3단 트리)** | $T_1 (0.3\,\text{m}), T_2 (1.2\,\text{m}), T_3 (1.8\,\text{m})$ | $\text{MAE} \le 1.0\,\text{K}, \text{RMSE} \le 1.5\,\text{K}$ | 국소 편차 $|\Delta T_{\max}| > 2.0\,\text{K}$ 또는 단일 센서 대표 |
| **타공 타일 풍량·하부 정압** | $Q_{\text{tile}}$ 및 $\Delta P_{\text{plenum}}$ | 배압 보상 발로미터 실측과 $\pm 10\%$ 이내 | 베르누이 역류($\Delta P_{\text{tile}} \le 0\,\text{Pa}$) 미재현 |
| **열부하 경계 조건 (하이브리드)** | $Q_{\text{air}} = P_{\text{elec}} - Q_{\text{liquid}}$ | 0.5S급 PDU 실측 전력과 CDU 열량 동시 기록 | 명판 정격 전력(Nameplate W) 직접 입력 |
| **기류 무차원 평가 지수** | $\text{SHI}, \text{RHI}, \text{RCI}_{\text{HI}}$ | $\text{SHI} < 0.15, \text{RHI} > 0.85, \text{RCI}_{\text{HI}} \ge 96\%$ | 컬러 스케일 왜곡을 통한 핫스팟 은폐 |

또한 하부 플레넘 내 수평 풍속이 $v_{\text{plenum}} > 4.5\,\text{m/s}$에 달하는 CRAH 토출구 직후 구간에서는 동압($\frac{1}{2}\rho v^2$) 증가로 인해 정압이 강하하여 첫 번째 타일에서 더운 공기가 역흡입된다. 컬러맵 스케일의 인위적 확장($15^\circ\text{C}\sim 45^\circ\text{C}$)을 통한 ASHRAE A1/A2 상한 초과 은폐 간파 원칙을 철저히 집행하고 모든 경계 조건을 서면으로 고정하라.

## 과도 응답·격자 독립성 및 현장 감사 절차

정상 상태(Steady-state) 컬러 컨투어 도면만으로는 냉각기 트립 시의 열적 여유(라이드스루 시간 $t_{\text{ride}}$)를 증명할 수 없다. CRAH $N-1$ 트립이나 칠러 재기동($180\sim 300\,\text{s}$) 비정상 해석에서는 서버 섀시 및 실내 공기의 유효 열용량과 온도 상승에 따른 서버 팬 회전수 급증(3제곱 법칙 $P_{\text{fan}} \propto N^3$)을 연성 해석해야 한다.

![3. 공기역학과 CFD 보고서 판독법](../figures/fig-04-hybrid-liquid-air-thermal-split.png)

$$\text{SHI} = \frac{\delta Q}{Q + \delta Q} = \frac{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{in}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{out}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}$$

1. **계측기 교정 및 좌표 고정**: 모든 Pt100 온도 프로브, 미차압계, 발로미터의 유효 교정 성적서 번호를 Sheet 1에 기록하고 CAD 도면 리비전 일자와 측정 일시를 동기화한다.
2. **격자 수렴성(GCI) 확인**: 거친 격자와 조밀한 격자의 비교를 통해 주요 흡기 온도 변화가 $0.25\,\text{K}$ 미만임을 Sheet 2에서 검증한다.
3. **조건부 기술 판정 서명**: 검증된 부하·풍량 범위를 명시하고, 그 경계 밖으로의 외삽이나 물리적 커미셔닝 생략 요구를 공식 거부한다.

$$\text{RHI} = \frac{Q}{Q + \delta Q} = 1 - \text{SHI}$$

$$\text{RCI}_{\text{HI}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{in}, i} - T_{\text{max, rec}}\right)}{N \cdot \left( T_{\text{max, allow}} - T_{\text{max, rec}} \right)} \right] \times 100\%$$

$$\text{RCI}_{\text{LO}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{min, rec}} - T_{\text{in}, i}\right)}{N \cdot \left( T_{\text{min, rec}} - T_{\text{min, allow}} \right)} \right] \times 100\%$$

$$\text{CI}_{\text{cold}, i} = \frac{\sum_{t} \dot{m}_{i, t}^{\text{tile}\to\text{rack}}}{\dot{m}_i^{\text{rack}}}, \qquad \text{CI}_{\text{hot}, i} = \frac{\sum_{c} \dot{m}_{i, c}^{\text{rack}\to\text{CRAH}}}{\dot{m}_i^{\text{rack}}}$$

$$\Delta P_{\text{CAC}} = \frac{\rho_{\text{air}}}{2} \left( \frac{\sum Q_{\text{CRAH}} - \sum Q_{\text{server}}}{C_d \cdot A_{\text{containment\_leak}}} \right)^2 \in [+1.5\,\text{Pa}, \, +5.0\,\text{Pa}]$$

## 기록해야 할 결정 사항

- 대상 홀의 감사 초점(공급 공기 분배 지수($\text{SHI} < 0.15$), 환기 열회수 지수($\text{RHI} > 0.85$), 랙 냉각 지수($\text{RCI}_{\text{HI}} \ge 96\%$) 및 아르키메데스 수($\text{Ar}$)를 통한 부력 대 관성 지배 판정) 및 CAD 지오메트리 동결일 기록.
- 교정된 계측기에 의한 현장 실측값(서버 팬 곡선 $P$-$Q$와 컨테인먼트 차압($+2.5\,\text{Pa} \sim +12.0\,\text{Pa}$)의 연성 해석)과 CFD 수치 프로브의 오차 검증(MAE $\le 1.0\,\text{K}$).
- 하이브리드 액체 냉각 랙에서 PDU 유효전력과 CDU 액체측 열제거량의 차감 계산 증빙.
- 불합격 조건(컬러맵 스케일의 인위적 확장($15^\circ\text{C}\sim 45^\circ\text{C}$)을 통한 ASHRAE A1/A2 상한 초과 은폐 간파) 해당 시 즉시 반려 및 Sheet 1·Sheet 2 서명.
