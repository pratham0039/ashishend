from bs4 import BeautifulSoup

html_content = """

<a href='https://www.youtube.com/watch?v=KfCIX_NizUI'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (16).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Tribal Story: Ikra Rasool, Chiral, Reasi along with teacher Iqbal Hussein.</h5>
                            <div data-href="https://www.youtube.com/watch?v=KfCIX_NizUI"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=iMpBp704O2E'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (17).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Altaf Ahmed Altaf</h5>
                            <div data-href="https://www.youtube.com/watch?v=iMpBp704O2E"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=sAbMam-kyBs'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (18).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Dr. Javaid Rahi, Editor at Jammu and Kashmir Academy of Art, Culture & Languages.</h5>
                            <div data-href="https://www.youtube.com/watch?v=sAbMam-kyBs"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=zOAJ6krbe6I'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (19).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">A Gujjar Shephard and his local tunes</h5>
                            <div data-href="https://www.youtube.com/watch?v=zOAJ6krbe6I"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=OKToliCVX9k'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (20).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Aftab Ahmed Aftab</h5>
                            <div data-href="https://www.youtube.com/watch?v=OKToliCVX9k"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=qcldajPlb_4'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (21).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Altaf Ahmed Altaf</h5>
                            <div data-href="https://www.youtube.com/watch?v=qcldajPlb_4"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=6yjgbOHItzc'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (22).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Dr. Javaid Rahi, Editor at Jammu and Kashmir Academy of Art, Culture & Languages.</h5>
                            <div data-href="https://www.youtube.com/watch?v=6yjgbOHItzc"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=tQleH0b8iA0'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (23).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Dr. Javaid Rahi, Editor at Jammu and Kashmir Academy of Art, Culture & Languages.</h5>
                            <div data-href="https://www.youtube.com/watch?v=tQleH0b8iA0"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=DA7mOXfTjZ0'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (24).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Dr. Abdul Khabir, Deputy Director, Tribal Affairs Department Jammu</h5>
                            <div data-href="https://www.youtube.com/watch?v=DA7mOXfTjZ0"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=EtaB0-SmZ-s'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (1).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Waseem Anjum</h5>
                            <div data-href="https://www.youtube.com/watch?v=EtaB0-SmZ-s"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=qsSUfJeWAd0'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (25).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Haji Abdul Haq Awan</h5>
                            <div data-href="https://www.youtube.com/watch?v=qsSUfJeWAd0"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=nKlVBPKSXH0'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (26).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Wasim Anjum, Gojri Lok Geet</h5>
                            <div data-href="https://www.youtube.com/watch?v=nKlVBPKSXH0"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=qujHhKw-jB8'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (27).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Geet by Kharsheda Begum</h5>
                            <div data-href="https://www.youtube.com/watch?v=qujHhKw-jB8"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=zTJn2bbyAa4'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (28).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Geet by Wasim Anjum</h5>
                            <div data-href="https://www.youtube.com/watch?v=zTJn2bbyAa4"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=1Iofyp02k_A'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (29).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Surjeet Singh Pardesi ji</h5>
                            <div data-href="https://www.youtube.com/watch?v=1Iofyp02k_A"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=gU5UP1otLec'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (30).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Surjeet Singh Pardesi Ji</h5>
                            <div data-href="https://www.youtube.com/watch?v=gU5UP1otLec"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=j6jKe7umCHg'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (2).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet By  Surjeet ji</h5>
                            <div data-href="https://www.youtube.com/watch?v=j6jKe7umCHg"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=GmXoodC3MIE'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (3).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Kharsheda Begum</h5>
                            <div data-href="https://www.youtube.com/watch?v=GmXoodC3MIE"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=spLqcqN6sjs'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (4).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Surjit Singh</h5>
                            <div data-href="https://www.youtube.com/watch?v=spLqcqN6sjs"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=FTZDJf5XJ0g'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (5).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet By Surjeet Singh</h5>
                            <div data-href="https://www.youtube.com/watch?v=FTZDJf5XJ0g"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=_usiyp2wykk'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (31).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet Comprehension by Mohd Naseem Gulabgari</h5>
                            <div data-href="https://www.youtube.com/watch?v=_usiyp2wykk"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=tjHikVyN6nQ'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (32).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet By Altaf ji</h5>
                            <div data-href="https://www.youtube.com/watch?v=tjHikVyN6nQ"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=3lCZJQDxa6s'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (33).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Alia Kousar, Heena Kousar, and Tabya Kousar</h5>
                            <div data-href="https://www.youtube.com/watch?v=3lCZJQDxa6s"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=1F3cXT16I2s'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (34).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Mushtaq Ahmed</h5>
                            <div data-href="https://www.youtube.com/watch?v=1F3cXT16I2s"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=0plozjHSay4'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (35).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri geet by Rakha Devi and Manisha Devi</h5>
                            <div data-href="https://www.youtube.com/watch?v=0plozjHSay4"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=wo4QbNgG3HI'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (36).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Mohd Naseem Gulabgari</h5>
                            <div data-href="https://www.youtube.com/watch?v=wo4QbNgG3HI"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=GnwpRihrjNk'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (37).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet by Mushtaq Ahmed Mushtaq</h5>
                            <div data-href="https://www.youtube.com/watch?v=GnwpRihrjNk"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=5MMeRpOioOU'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (38).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Mohd Rafiq</h5>
                            <div data-href="https://www.youtube.com/watch?v=5MMeRpOioOU"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=dS_BlXuNTBI'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (39).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet by  Mushtaq Ahmed</h5>
                            <div data-href="https://www.youtube.com/watch?v=dS_BlXuNTBI"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=sTwAm9LgAjo'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (40).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet By Imtayaz Ahmed</h5>
                            <div data-href="https://www.youtube.com/watch?v=sTwAm9LgAjo"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=951SZx8Qurc'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (41).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet By Mohd. Rafi</h5>
                            <div data-href="https://www.youtube.com/watch?v=951SZx8Qurc"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=bIisyhQ1zoY'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (42).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Mohd Mashooq and Laqatat Ali</h5>
                            <div data-href="https://www.youtube.com/watch?v=bIisyhQ1zoY"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=CwheXunvsSQ'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (43).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet by Mohd. Shafi</h5>
                            <div data-href="https://www.youtube.com/watch?v=CwheXunvsSQ"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=Wxv21jZ2Wwc'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (44).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Mohd Shafi, Life of Gujjar Community</h5>
                            <div data-href="https://www.youtube.com/watch?v=Wxv21jZ2Wwc"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=viqt-KOoKHU'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (9).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Wasim Anjum</h5>
                            <div data-href="https://www.youtube.com/watch?v=viqt-KOoKHU"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=ngvrYHxnn1M'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (45).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Wasim Anjum</h5>
                            <div data-href="https://www.youtube.com/watch?v=ngvrYHxnn1M"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=tSnXdDwMIvk'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (46).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet By Sher Singh</h5>
                            <div data-href="https://www.youtube.com/watch?v=tSnXdDwMIvk"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=e0ffg_sH1SE'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (47).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet at Majra Kund, Reasi</h5>
                            <div data-href="https://www.youtube.com/watch?v=e0ffg_sH1SE"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=Q7UjCf2HQr0'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (48).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lookgeet at Majra Kund, Mahore, Reasi</h5>
                            <div data-href="https://www.youtube.com/watch?v=Q7UjCf2HQr0"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=WZe3vkEs4dg'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (49).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lok Geet by Molvi Jameel</h5>
                            <div data-href="https://www.youtube.com/watch?v=WZe3vkEs4dg"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=NNl3J28LIyI'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (50).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet at Gotu, Block Budhal.</h5>
                            <div data-href="https://www.youtube.com/watch?v=NNl3J28LIyI"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=En__wXMSR9U'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (51).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet at Gotu, Block Budhal.</h5>
                            <div data-href="https://www.youtube.com/watch?v=En__wXMSR9U"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=EULCuN3wuhE'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (52).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Local Gujjar Children</h5>
                            <div data-href="https://www.youtube.com/watch?v=EULCuN3wuhE"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=-BRczbX9f8M'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/mqdefault_6s (53).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet at Gotu, Block Budhal. Introduction of the Artist.</h5>
                            <div data-href="https://www.youtube.com/watch?v=-BRczbX9f8M"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=zgD7m2vr6t4'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (7).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Lokgeet by Molvi Jameel</h5>
                            <div data-href="https://www.youtube.com/watch?v=zgD7m2vr6t4"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>   <a href='https://www.youtube.com/watch?v=OOKY_hnFCwY'>
                        <div class="col-xs-6 col-sm-4 col-md-3" style="padding: 0px">
                            <img class="img-responsive img-thumbnail docview" style="padding: 1px" src='images/hqdefault (8).webp' height="200px" width="250px" >
                            <div class="play">
                                <img class="img-responsive" src="dist/img/youtube.png" />
                            </div>

                            <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Gojri Look Geet by Molvi Jameel</h5>
                            <div data-href="https://www.youtube.com/watch?v=OOKY_hnFCwY"></div>
                            <br />
                            <br />
                            
                        </div>
                    </a>  


"""
import pandas as pd
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
data = []

# Find all <a> tags with class "yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media"
a_tags = soup.find_all('a')

# Extract and print the title from each <a> tag
for a_tag in a_tags:
    title = a_tag['href']
    print("Title:", title)
    data.append({'Title': title, 'Text': ''})

h5_tags = soup.find_all('h5')

# Extract and print the inner text from each <h5> tag
for h5_tag in h5_tags:
    inner_text = h5_tag.text
    print("Inner Text:", inner_text)
    data.append({'Title': '', 'Text': inner_text})

df = pd.DataFrame(data)

# Export DataFrame to CSV
csv_file = 'data.csv'
df.to_csv(csv_file, index=False)