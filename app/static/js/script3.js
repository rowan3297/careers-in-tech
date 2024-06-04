var RangeSlider = function(containerID) {
    var self = this,
        $RangeSlider = $('#'+containerID),
        $SliderThumnb = $RangeSlider.find('.RangeSlider_Thumb'),
        $SliderTrack = $RangeSlider.find('.RangeSlider_Track'),
        $SliderTrackFill = $RangeSlider.find('.RangeSlider_TrackFill'),
        $ClickArea = $RangeSlider.find('.RangeSlider_ClickArea'),
        $SliderPoints = $RangeSlider.find('.RangeSlider_Point');
    
    this.value = 0;
      
    /* helper to find slider value based on filled track width */
    var findValueFromTrackFill = function(trackFillWidth) {
      var totalWidth = $SliderTrack.width(),
          onePercentWidth = totalWidth / 100,
          value = Math.round((trackFillWidth / onePercentWidth) / 10);
      return value;
    }
    
    /* change highlighted number based on new value */
    var updateSelectedValue = function(newValue) {
      $SliderPoints.removeClass('RangeSlider_PointActive');
      $SliderPoints.eq( newValue ).addClass('RangeSlider_PointActive');
      this.value = newValue
    //   var changeDivs = document.querySelectorAll('.change');
    //     changeDivs.forEach(div => {
    //         div.innerText = rangeSlider.value
    //     })
    }
    
    /* highlight track based on new value (and move thumb) */
    var updateHighlightedTrack = function(newPosition) {
      newPosition = newPosition + '0%';
      $SliderTrackFill.css('width', newPosition);
    }
    
    /* set up drag funcationality for thumbnail */
    var setupDrag = function($element, initialXPosition) {
      $SliderTrackFill.addClass('RangeSlider_TrackFill-stopAnimation');
      var trackWidth = $SliderTrackFill.width();
      
      var newValue = findValueFromTrackFill( trackWidth );
      updateSelectedValue(newValue);
      
      $element.on('mousemove', function(e){
        var newPosition = trackWidth + e.clientX - initialXPosition;
        self.imitateNewValue( newPosition );
        
        newValue = findValueFromTrackFill( $SliderTrackFill.width() );
        updateSelectedValue(newValue);
      });
    }
    /* remove drag functionality for thumbnail */
    var finishDrag = function($element) {
      $SliderTrackFill.removeClass('RangeSlider_TrackFill-stopAnimation');
      $element.off('mousemove');
      var newValue = findValueFromTrackFill( $SliderTrackFill.width() );
      self.updateSliderValue( newValue );
    }
    
    /* method to update all things required when slider value updates */
    this.updateSliderValue = function(newValue) {
      updateSelectedValue( newValue );
      updateHighlightedTrack( newValue );
      self.value = newValue;
      console.log('this.value = ', self.value);
    }
    
    /* method to imitate new value without animation */
    this.imitateNewValue = function(XPosition) {
      $SliderTrackFill.addClass('RangeSlider_TrackFill-stopAnimation');
      if ( XPosition > $SliderTrack.width() ) {
        XPosition = $SliderTrack.width();
      }
      $SliderTrackFill.css('width', XPosition + 'px');
    }
    
    /*
     * bind events when instance created
     */
    $ClickArea.on('mousedown', function(e){
      /* if a number or thumbnail has been clicked, use their event instead */
      var $target = $(e.target);
      if ( $target.hasClass('RangeSlider_Thumb') ) {
        return false;
      }
      /* now we can continue based on where the clickable area was clicked */
      self.imitateNewValue( e.offsetX );
      setupDrag( $(this), e.clientX );
    });
    
    $ClickArea.on('mouseup', function(e){
      console.log('"$ClickArea" calling "finishDrag"');
      finishDrag( $(this) );
    });
    
    // update value when markers are clicked
    $SliderPoints.on('mousedown', function(e){
      e.stopPropagation();
      var XPos = $(this).position().left + ($(this).width()/2);
      self.imitateNewValue( XPos );
      setupDrag( $ClickArea, e.clientX );
    });
    
    // when thumbnail is clicked down, init the drag stuff
    $SliderThumnb.on('mousedown', function(e){
      e.stopPropagation();
      setupDrag( $(this), e.clientX );
    });
    
    // when the thumbnail is released, remove the drag stuff
    $SliderThumnb.on('mouseup', function(e){
      console.log('"$SliderThumnb" calling "finishDrag"');
      finishDrag( $(this) );
    });
  }
  
  var rangeSlider = new RangeSlider('RangeSlider');
  var rangeSlider2 = new RangeSlider('RangeSlider2');
  var rangeSlider3 = new RangeSlider('RangeSlider3');
  var rangeSlider4 = new RangeSlider('RangeSlider4');
  var rangeSlider5 = new RangeSlider('RangeSlider5');
  var rangeSlider6 = new RangeSlider('RangeSlider6');
  var rangeSlider7 = new RangeSlider('RangeSlider7');
  var rangeSlider8 = new RangeSlider('RangeSlider8');
  var rangeSlider9 = new RangeSlider('RangeSlider9');
  var rangeSlider10 = new RangeSlider('RangeSlider10');
  var rangeSlider11 = new RangeSlider('RangeSlider11');
  var rangeSlider12 = new RangeSlider('RangeSlider12');
  var rangeSlider13 = new RangeSlider('RangeSlider13');

let mouseMoved = false;
const button = document.querySelector('.infoButton');

const mouseMoveHandler = event => {
    clearInterval(loop);
    document.onmousemove = null;
    button.classList.remove('infoButton_isActive');
};

const toggleHandler = event => {    
    const classes = button.classList;
    if (classes.contains('infoButton_isActive')) {
        classes.remove('infoButton_isActive');
    } else {
        classes.add('infoButton_isActive');
    }
}

document.onmousemove = mouseMoveHandler;

const loop = setInterval(toggleHandler, 1000);

// function updateValue(skillId) {
//     const value = document.getElementById(skillId).value;
//     document.getElementById(`${skillId}-value`).innerText = value;
// }

function storeSkillsAndRedirect() {
    const userSkills = {
        A: rangeSlider.value,
        B: rangeSlider2.value,
        C: rangeSlider3.value,
        D: rangeSlider4.value,
        E: rangeSlider5.value,
        F: rangeSlider6.value,
        G: rangeSlider7.value,
        H: rangeSlider8.value,
        I: rangeSlider9.value,
        J: rangeSlider10.value,
        K: rangeSlider11.value,
        L: rangeSlider12.value,
        M: rangeSlider13.value

    };

    localStorage.setItem('userSkills', JSON.stringify(userSkills));
    
}


// var activeValue = 0
// var sliderActive = document.querySelectorAll('.RangeSlider_PointActive');
// sliderActive.forEach(div => {
//     activeValue = div.innerText;
// })

// Select the button with class "infoButton"
// var infoButton = document.querySelector('.infoButtons');

// // Add an event listener to the button
// infoButton.addEventListener('click', function() {
//   // The highlighted code
//   var changeDivs = document.querySelectorAll('.change');
//   changeDivs.forEach(div => {
//     div.innerText = rangeSlider2.value;
//   });
// });

// document.querySelector('.back-button').addEventListener('click', function() {
//   window.history.back();
// });